from django.contrib.auth import views as auth_views
from django.urls import path, re_path, reverse_lazy

from .views import (
    register_view,
    logout_view,
    login_view,
    AccountEmailActivateView,
    user_profile
)

app_name = "account"

urlpatterns = [

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user-profile', user_profile, name="user-profile"),

    # For email confirm & activation
    re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),
    re_path(r'^email/resend-activation/$', AccountEmailActivateView.as_view(), name='resend-activation'),

    # Password Reset urls
    # path('reset/', auth_views.PasswordResetView.as_view(
    #     template_name='accounts/register/password_reset.html',
    #     email_template_name='accounts/register/password_reset_email.html',
    #     subject_template_name='accounts/register/password_reset_subject.txt'), name='password_reset'),

    path('reset/', auth_views.PasswordResetView.as_view(

        template_name='accounts/register/password_reset.html',
        email_template_name='accounts/register/password_reset_email.html',
        subject_template_name='accounts/register/password_reset_subject.txt',
        success_url=reverse_lazy('account:password_reset_done'))
         , name='password-reset'
         ),

    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/register/password_reset_done.html'), name='password_reset_done'),

    # path('register-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='accounts/register/password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/register/password_reset_confirm.html',
             # success_url="reset/complete/",
             success_url=reverse_lazy('account:password_reset_complete'),
             post_reset_login=True),
         name='password_reset_confirm'),

    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/register/password_reset_complete.html'), name='password_reset_complete'),

    # path('settings/register/', auth_views.PasswordChangeView.as_view(
    #     template_name='accounts/register/password_change.html'),
    #      success_url=reverse_lazy('account:password_change_done'),
    #      name='password_change'
    #      ),

    # change password urls
    # path('password-change/', auth_views.PasswordChangeView.as_view(
    #
    # ), template_name='accounts/register/password_change.html',
    #      success_url=reverse_lazy('account:password_change_done'),
    #      name='password_change'
    #      ),

    # Password Changes URLs
    # path('password_change/', auth_views.PasswordChangeView.as_view(
    #     success_url=reverse_lazy('account:password_change_done')
    # ), name='password_change'),

    path('password-change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done'),
                                               template_name='accounts/register/password_change.html'),
         name='password_change'),

    path('settings/register/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/register/password_change_done.html'), name='password_change_done'),
]
