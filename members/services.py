from django.contrib.auth.models import Group
from django.db.models import Sum

from members.models import Endorsement

PLEB = 10000
SUPER_SPONSOR = 100000
INNER_CIRCLE = 150000
NO_LIFER = 1000000


def amount_calculation_and_tear_check(instance):
    current_sponsor = instance.sponsor
    total_amount = Endorsement.objects.filter(sponsor=current_sponsor).aggregate(total=Sum('amount'))['total'] or 0
    if total_amount <= PLEB:
        tier = 'pleb'
    elif total_amount <= SUPER_SPONSOR:
        tier = 'super_sponsor'
    elif total_amount <= INNER_CIRCLE:
        tier = 'inner_circle'
    else:
        tier = 'no_lifer'
    return [tier, total_amount]


"""
this one uses signals 
"""


def tier_choose(instance, tier):
    user = instance.sponsor
    if tier == 'pleb':
        user.groups.set([])
        return
    TIER_GROUPS = {
        'pleb': 'Pleb',
        'super_sponsor': 'Super Sponsor',
        'inner_circle': 'Inner Circle',
        'no_lifer': 'No Lifer'
    }
    group_to_add = Group.objects.get(name=TIER_GROUPS.get(tier))
    user.groups.set([group_to_add])
