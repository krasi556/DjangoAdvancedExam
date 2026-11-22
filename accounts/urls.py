from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/',views.Login.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('password-reset/', PasswordResetView.as_view(  # sends it to the email  MUST INCLUDE EMAIL HTML
        email_template_name='account/password-reset-email.html',
        template_name='account/password-reset.html',
        success_url=reverse_lazy('accounts:password-reset-done')
    ), name='password-reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(  # is jsut a confirmation that the email was sent
        template_name='account/password-reset-done.html',
    ), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/',  # ACTUAL PASSWORD CHANGE IS HAPPENING HERE ! MUST HAVE FORM
         PasswordResetConfirmView.as_view(
             template_name='account/password-reset-confirm.html',
             success_url=reverse_lazy('core:redirect-home'),
             post_reset_login=True
         ), name='password-reset-confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        # JUST THE CONFIRMATION AFTER CHANGING THE EMAIL
        # template_name='account/password-reset-complete.html',
    ), name='password-reset-complete'),
    path('password-change/', PasswordChangeView.as_view(
        template_name='account/password-change.html',
        success_url=reverse_lazy('accounts:password-change-done'),
    ), name='password-change'),
    path('password-successfuly-changed/', PasswordChangeDoneView.as_view(
        template_name='account/password-change-done.html'
    ), name='password-change-done'),
    path('user-reviews/', views.user_reviews, name ='user-reviews'),
    path('delete-user/',views.DeleteUserProfile.as_view(),name='delete-user'),


]
