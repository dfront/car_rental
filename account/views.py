#-*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout
from account.forms import LoginForm
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from account.authentication import QuietBasicAuthentication
from account.serializers import UserSerializer
import logging
logger = logging.getLogger(__name__)

class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    logger.error("######xiiiii#########")
    
    def post(self, request, *args, **kwargs):
        logger.error("##################")
        login(request,request.user)
        return Response(UserSerializer(request.user).data)
  
    def delete(self, request, *args, **kwargs):
        logger.error("$$$$$$$$$$$$$$$$$")
        logout(request)
        return Response({})


def LoginView(request):
    login_form = LoginForm()   
    c = {"login_form":login_form}
    return render_to_response("account/login.html",c)
