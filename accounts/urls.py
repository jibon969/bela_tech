from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
# from accounts.views import (
#     LoginView,
#     signup,
#     app_user,
#     app_user_csv
# )
#
# from .views import (
#     AccountEmailActivateView,
#     UserDetailUpdateView
# )

app_name = 'account'

urlpatterns = [


    # url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    #
    # # From Product Apps
    # url(r'history/products/$', UserProductHistoryView.as_view(), name='user-product-history'),
    #
    # url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$',
    #     AccountEmailActivateView.as_view(),
    #     name='email-activate'),
    # url(r'^email/resend-activation/$',
    #     AccountEmailActivateView.as_view(),
    #     name='resend-activation'),
    #
    # # Login & register urls
    # path('login/', LoginView.as_view(), name='login'),
    # path('register/', signup, name='register'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password-reset'),
    #
    # path('app-user/', app_user, name="app-user"),
    # path('app-user-csv/', app_user_csv, name="app-user-csv")
]
