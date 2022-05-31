from sys import settrace
from turtle import forward
from django.shortcuts import render
from .serializers import IssueSerializers, UserIssueSerializers
from .models import Issue
# Create your views here.
from django.http import HttpResponse

from django.contrib.auth import get_user_model
User = get_user_model()



from rest_framework.decorators import APIView
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from . serializers import UserSeralizer

from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

class IssueView(viewsets.ModelViewSet):
    # user = User.objects.all()
    queryset = Issue.objects.all()
    serializer_class = IssueSerializers
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['Reporting_person']
    # def get_object(self):
    #     obj = get_object_or_404(self.get_queryset(),pk = self.kwargs["pk"])


    @action(detail=True,methods=['GET'])
    def assigned(self,request,pk):
        # queryset = Issue.objects.all()
        # import ipdb;ipdb.set_trace()
        # for x in queryset:
        # getissue = self.get_object()
        # assigned_issue = Issue.objects.filter(self.user==self.request.user)


        # serializer = self.get_serializer(assigned_issue,many = True)
        serializer = self.get_serializer(self.user==pk,many = True)
        
        return Response(serializer)


    @action(detail=True, methods=['GET','PUT'])
    def forward_issue(self,request, pk=None):
        """
        Params : level
        """
        level = request.GET.get('level', None) # for get request 
        # level = request.data.get()

        print('===================',level)

        if pk and level:

            issue_obj= Issue.objects.get(pk=pk )
            issue_obj.level = level
            issue_obj.save()
            return Response({"message":"Done"})

        print('Nooo')




class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # import ipdb;ipdb.set_trace()
    serializer_class = UserSeralizer

    @action(detail=False, methods=['GET'])
    def assigned(self,request,pk):
        # queryset = User.objects.all()
        
        issueid = Issue.objects.all()

        user_data = Issue.objects.filter(level= self.request.user.user_level)


        # serializer = self.get_serializer(pk=pk)
        serializer = IssueSerializers(user_data,many=True)
        
        return Response(serializer.data)
    @action(detail=True, methods=['GET','PUT'])
    def forward_issue(self,request, pk=None):
        issue_id = request.GET.get('issue', None)
        print('===================',request.GET)

        if pk and issue_id:

            user= User.objects.get(pk=pk )
            issue_obj = Issue.objects.get(id=issue_id)
            issue_obj.level = user.user_level
            issue_obj.save()
            return Response({"message":"Done"})

        print('Nooo')



    
class UserIssueView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserIssueSerializers



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.decorators import renderer_classes


@api_view(['GET', 'POST', 'DELETE','UPDATE'])
@renderer_classes([JSONRenderer,BrowsableAPIRenderer])
def serializerIssue(request, pk):
    try:
        user_data = User.objects.get(pk=pk)
        
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    issuedata= Issue.objects.all()

    if request.method == 'GET':
        serializer = UserSeralizer(user_data)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserIssueSerializers(data=request.data,pk = pk)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




















'''commented for re use'''

# class UserView(generics.ListAPIView,generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSeralizer