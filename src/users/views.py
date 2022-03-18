from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from users.serializers import *
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from users.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from core.mixin import LoggingMixin
from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer

from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.social_serializers import TwitterLoginSerializer

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
class UserViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = UserModel.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def user_exist(request):
    """
    Allows unauthenticated user to checks if a user exist in the system. request = {username: $username} ,  return True/False
    """
    keys = request.data.keys()
    exist = False
    if len(keys) > 0:
        if keys.__contains__('username'):
            if UserModel.objects.filter(username = request.data['username'],).exists():
                exist = True
        elif  keys.__contains__('email'):
              if  UserModel.objects.filter(email = request.data['email'],).exists():
                   exist = True
        elif keys.__contains__('phone'):
              if  UserModel.objects.filter(phone = request.data['phone'],).exists():
                   exist = True
    return Response({"exist": exist}, requests.codes.ok)


class UserDocumentViewSet(LoggingMixin, viewsets.ModelViewSet):
    """
    API endpoint to set or update user documents
    """
    serializer_class = UserDocumentSerializer

    def get_queryset(self):
        return UserDocument.objects.filter(owner=self.request.user).order_by("pk")


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited
#     """
#     queryset = Group.objects.all().order_by()
#     serializer_class = GroupSerializer



# SOCIAL  ACCOUNT AUTHENTICATION 
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter

class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter