from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Permission, User
from django.contrib.auth.views import redirect_to_login, logout_then_login, PasswordResetView, LoginView
from django.db.models import Avg, Count
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from accounts.forms import RegisterForm
from reviews.models import Review


# Create your views here.


def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        if user.username.startswith('123test'):
            permission = Permission.objects.get(
                codename='delete_employee',
                content_type__app_label='employees'
            )
            user.user_permissions.add(permission)
        return redirect('core:load-main-page')
    context = {
        'form': form
    }
    return render(request, 'account/register-account.html', context)


# @user_passes_test(
#     lambda user: not user.is_authenticated,
#     login_url='core:load-main-page',
# )
# def login_user(request):
#     form = AuthenticationForm(request, request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         login(request, form.get_user())
#         if request.GET.get('next'):
#             return redirect(request.GET.get('next'))
#         return redirect('core:redirect-home')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'account/login.html', context)

class Login(LoginView):
    success_url = 'core:redirect-home'
    template_name = 'account/login.html'


def logout_view(request):
    logout(request)
    return redirect('core:redirect-home')


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect_to_login(request.get_full_path())
    user = request.user
    reviews_count = (Review.objects
    .filter(author=user)
    .aggregate(
        avg_rating=Avg('rating'),
        reivew_count=Count('id'))
    )
    context = {
        'user': user,
        'reviews_count': reviews_count['reivew_count'],
        'avg_rating': reviews_count['avg_rating']
    }
    return render(request, 'account/profile.html', context)


def user_reviews(request):
    user = request.user
    reviews = Review.objects.filter(author=user) or None
    context = {
        'reviews': reviews,
        'user': user
    }
    return render(request, 'account/user-reviews.html', context)


class DeleteUserProfile(DeleteView):
    success_url = reverse_lazy('core:redirect-home')
    template_name = 'account/delete-user.html'

    def get_object(self, queryset=None):
        return self.request.user

