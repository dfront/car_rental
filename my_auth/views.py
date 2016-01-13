#-*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from account.forms import LoginForm
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from account import authentication, serializers 

class AuthView(APIView):
    authentication_classes = (authentication.QuietBasicAuthentication,)
    serializer_class = serializers.UserSerializer
 
    def post(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)

def login(request):
    login_form = LoginForm()   
    c = {"login_form":login_form}
    return render_to_response("account/login.html",c)
