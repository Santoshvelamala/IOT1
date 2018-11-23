# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Traffic,OverSpeed
# Create your views here.

@csrf_exempt
def traffic(request):
    t = Traffic(Route=request.POST['Route'], Density=request.POST['Density'], Date = request.POST['Date'])
    t.save()
    return HttpResponse("Logged in successfully")
@csrf_exempt
def overspeed(request):
    os = OverSpeed(Route=request.POST['Route'], Speed=request.POST['Speed'], Date = request.POST['Date'], Vehiclenum=request.POST['Vehiclenum'])
    os.save()
    return HttpResponse("Logged in successfully")

