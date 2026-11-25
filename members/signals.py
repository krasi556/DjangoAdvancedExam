from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import get_user
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from accounts.models import Profile
from members.models import Endorsement
from members.services import amount_calculation_and_tear_check, tier_choose

UserModel = get_user_model()


@receiver(post_save, sender=Endorsement)
def update_sponsor(sender, instance, created, **kwargs):
    tier, total_amount = amount_calculation_and_tear_check(instance)
    tier_choose(instance, tier)
    current_profile = instance.sponsor.profile
    current_profile.total_wasted = total_amount
    current_profile.tier = tier
    current_profile.save(update_fields=['total_wasted', 'tier'])


@receiver(post_delete, sender=Endorsement)
def delete_sponsor(sender, instance, **kwargs):
    if not Profile.objects.filter(pk=instance.sponsor_id).exists():
        return
    tier, total_amount = amount_calculation_and_tear_check(instance)
    tier_choose(instance, tier)
    current_profile = instance.sponsor.profile
    current_profile.total_wasted = total_amount
    current_profile.tier = tier
    current_profile.save(update_fields=['total_wasted', 'tier'])
