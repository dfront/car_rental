#-*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rent.models import Rent
from rent.forms import RentForm
from client.models import Client
from rent.serializers import RentSerializer
from vehicle.models import Vehicle
import logging
logger = logging.getLogger(__name__)


class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content  = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

@csrf_exempt
def rent_list(request):
    """
    List all code rents.
    """
    if request.method == 'GET':
        rents = Rent.objects.all()
        serializer = RentSerializer(rents, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@api_view(['POST'])
def rent_create(request):
    """
    Create a rent instance.
    """   
    if request.method == 'POST':
        serializer = RentSerializer(data=request.data)       
        #serializer.vehicle = Vehicle.objects.get(pk=request.data['vehicle']) queria fazer isso :-/
        #serializer.client = Client.objects.get(user=request.user)  // nao deu joguei o client no template X-|
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET'])
@login_required(login_url='/login/')
#@permission_classes((IsAuthenticated, ))
def home(request):   
    rent_form = RentForm()
    token = Token.objects.get_or_create(user=request.user,defaults={"user":request.user})
    client = Client.objects.get(user=request.user).id # nao deu joguei o client no template X-|
    c = {"rent_form":rent_form,"token":token[0],"client":client}
    return render_to_response("rent/rent.html",c)
