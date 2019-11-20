from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import scooters
from . serializers import scootersSerializer
from . serializers import BookScooterSerializer
import math
import requests
# Create your views here.

class scooterList(APIView):

    def get(self,request):
        scooterlist = scooters.objects.all()
        serializer = scootersSerializer(scooterlist,many=True)
        return Response(serializer.data)

#Will return NEAR BY SCOOTERS
class NearbyScooter(APIView):

    def get(self,request):

        radius = request.data['radius']
        lat = request.data['lat']
        long = request.data['long']

        scooter_locations = scooters.objects.all()
        available_scooter_list = list()

        for scooter in scooter_locations:
            cord1 = (lat,long)
            cord2 = (scooter.lat,scooter.long)

            distance = NearbyScooter.calculate(cord1,cord2)
            if distance < radius:
                available_scooter_list.append(scooter)

            if available_scooter_list:
                serializer = scootersSerializer(available_scooter_list,many=True)
            else:
                data = {"Unavailable": "Sorry, no scooters available at this time"}
                return Response(data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def calculate(self,cord1,cord2):
        r = 6371
        lat1,lon1=cord1[0],cord1[1]
        lat2,lon2= cord2[0],cord2[1]
        dlat = NearbyScooter.deg2rad(cord2[0]-cord1[0])
        dlong = NearbyScooter.deg2rad(cord2[1]-cord1[1])

        dist = (math.sin(dlat/2))**2 + math.cos(NearbyScooter.deg2rad(lat1)) * math.cos(NearbyScooter.deg2rad(lat2)) * math.sin(dlong/2) * math.sin(dlong/2)

        c = 2 * math.atan2(math.sqrt(dist), math.sqrt(1 - dist));
        d = r * c
        return d

    def deg2rad(self,deg):
        return deg * (math.pi / 180)

#WILL BOOK A SCOOTER
class BookScooter(APIView):

    """
    this function will request to book a scooter and arrange a ride.
    """
    def post(self,request):
        context = {'uniqueid':request.session['uniqueid'],
                   'source_address':request.session['source_address'],
                   'destination_address':request.session['destination_address']}
        serializer = BookScooterSerializer(data=request.data,context=context)
        if serializer.is_valid():
            serializer.save()
            data = {"Scooter booked, arriving"}
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)