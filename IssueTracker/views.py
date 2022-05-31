
from .serializers import IssueSerializers, UserIssueSerializers
from .models import Issue

from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import viewsets
from . serializers import UserSeralizer
from rest_framework.decorators import action
from rest_framework import mixins

#to check user is authenticated or not
from rest_framework.permissions import IsAuthenticated,IsAdminUser
class IssueView(viewsets.ModelViewSet,mixins.CreateModelMixin):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializers

    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(level=self.request.user.level)
        return qs



class UserView(mixins.ListModelMixin,
            mixins.UpdateModelMixin,
            viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSeralizer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSeralizer
    permission_classes = [IsAdminUser]




class UserIssueView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserIssueSerializers





# class AssignedIssue(viewsets.ModelViewSet):
#     user_id = User.objects.all()
#     queryset = Issue.objects.filter(recipent=user_id.id)
#     serializer_class = IssueSerializers(queryset,many =True)
#     # serializer = self.get_serializer(queryset,many = True)  
#     # return Response(serializer.data)

#     @action(detail=False,methods=['GET','PUT'])
#     def assigned(self,request,pk=None):
        
#         user_id = request.user
#         queryset = Issue.objects.filter(recipent=user_id.id)
#         assigned_issue = Issue.objects.filter(recipent=user_id.id)
#         print("------->",assigned_issue)
#         serializer = self.get_serializer(assigned_issue,many = True)  
#         return Response(serializer.data)

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



# "--------------"
        # queryset = Issue.objects.all()
        # import ipdb;ipdb.set_trace()
        # for x in queryset:
        # getissue = self.get_object()
        # assigned_issue = Issue.objects.filter(self.user==self.request.user)


        # serializer = self.get_serializer(assigned_issue,many = True)


    # user = User.objects.all()
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['Reporting_person']
    # def get_object(self):
    #     obj = get_object_or_404(self.get_queryset(),pk = self.kwargs["pk"])
            
    # @action(detail=True, methods=['PUT'])
    # def forward_issue(self,request, pk=None):
    #     """
    #     Params : level
    #     """
    #     level = request.GET.get('level', None) # for get request 
    #     if pk and level:
    #         issue_obj= Issue.objects.get(pk=pk )
    #         issue_obj.level = level
    #         issue_obj.save()
    #         return Response({"message":"Done"})

        # @action(detail=True,methods=['GET','PUT'])
    # def assigned(self,request):
    #     user_id = request.user.id
    #     assigned_issue = Issue.objects.filter(recipent=user_id)
    #     print("------->",assigned_issue)
    #     serializer = self.get_serializer(assigned_issue,many = True)  
    #     return Response(serializer.data)
