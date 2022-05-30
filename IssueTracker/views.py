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

from django.shortcuts import get_object_or_404


# @APIView(['GET'])
class IssueView(generics.CreateAPIView,
                generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['Reporting_person']
    def get_object(self):
        obj = get_object_or_404(self.get_queryset(),pk = self.kwargs["pk"])

class UserView(generics.ListAPIView,
               generics.CreateAPIView):
    queryset = User_Types.objects.all()
    serializer_class = UserSeralizer
    
class UserIssueView(generics.ListAPIView,
                    generics.CreateAPIView):
    queryset = User_Types.objects.all()
    serializer_class = UserIssueSerializers


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'PUT', 'DELETE','UPDATE'])
def serializerIssue(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = User_Types.objects.get(pk=pk)
        
    except User_Types.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    issuedata= Issue.objects.all()
    if request.method == 'GET':
        serializer = UserSeralizer(snippet)
        return Response(serializer.data)

    elif request.method == 'UPDATE':
        serializer = UserIssueSerializers(issuedata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)