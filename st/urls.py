from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_auth.views import (LoginView, LogoutView, UserDetailsView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView)
from . import views
from rest_framework.authtoken import views as rest_framework_views
from rest_framework import renderers



urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^register/$', views.CreateUserView.as_view(), name='create_user'),
    url(r'^keyword/$', views.StoreKeyword.as_view(), name='create_keyword'),
]

urlpatterns = format_suffix_patterns(urlpatterns)