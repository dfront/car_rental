from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content  = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

@csrf_exempt
def vehicle_list(request):
    """
    List all code vehicles
    """
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def vehicle_detail(request, pk):

    try:
        snippet = Vehicle.objects.get(pk=pk)
    except Vehicle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VehicleSerializer(vehicle)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehicleSerializer(vehicle, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vehicle.delete()
        return HttpResponse(status=204)
