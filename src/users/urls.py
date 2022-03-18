from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from .views import *
from rest_framework.schemas import get_schema_view
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

schema_view = get_schema_view(title='Authentication')

router = routers.DefaultRouter()
router.register('users', UserViewSet)
# router.register('groups', views.GroupViewSet)
router.register('documents', UserDocumentViewSet, basename='userdocument')
# router.register('user-account', view_set.UAccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('user-exist', user_exist),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    # path('auth/token/', obtain_jwt_token),
    # path('auth/token/refresh/', refresh_jwt_token),
    # path('auth/token/verify/', verify_jwt_token),
    # path('auth/facebook/', viewsets.FacebookLogin.as_view(), name='fb_login'),
    # path('auth/twitter/', viewsets.TwitterLogin.as_view(), name='twitter_login'),
    # path('auth/facebook/connect/', viewsets.FacebookConnect.as_view(), name='fb_connect'),
    # path('auth/twitter/connect/', viewsets.TwitterConnect.as_view(), name='twitter_connect'),
    # path('socialaccounts/', SocialAccountListView.as_view(), name='social_account_list'),
    # path('socialaccounts/<pk>/disconnect/', SocialAccountDisconnectView.as_view(),name='social_account_disconnect'),
    path('schema/', schema_view)
]