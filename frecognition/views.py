from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.template import loader
import json

from rest_framework import viewsets
from .models import Image
from .serializer import ImageSerializer


def index(request):
    return HttpResponse("Hello world")
