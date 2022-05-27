from django.shortcuts import render
from . serializers import IssueSerializers, UserIssueSerializers
from . models import Issue,User_Types
# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello world")


from rest_framework.decorators import APIView
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from . serializers import UserSeralizer
# from .forms import MyUserCreationForm




# @APIView(['GET'])
class IssueView(generics.CreateAPIView,
                generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['Reporting_person']

class UserView(generics.ListAPIView,
               generics.CreateAPIView):
    queryset = User_Types.objects.all()
    serializer_class = UserSeralizer
    
class UserIssueView(generics.ListAPIView,
                    generics.CreateAPIView):
    queryset = User_Types.objects.all()
    serializer_class = UserIssueSerializers