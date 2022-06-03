from ipaddress import v4_int_to_packed
from urllib import request
from rest_framework import serializers
from traitlets import default
from . models import LEVEL, User,Issue
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class IssueSerializers(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id','status_code','module','level','priority','company_name','description','status','upload_file']
    
        read_only_fields = ('is_active','is_staff')

    def create(self, validated_data):
        validated_data['level']='1'
        validated_data['status']='pending'
        validated_data['user_id']= self.context['user']
        return super().create(validated_data)
    def update(self, instance, validated_data):
        status = validated_data['status']
        level=validated_data['level']
        if status == "solved":
            # import ipdb;ipdb.set_trace()
            validated_data['level']=0
        elif status=='forward':
            if level==3:
                raise serializers.ValidationError('level 3 can not forward')    
            elif level==0:
                raise serializers.ValidationError('you do not have permission to do this action')
            validated_data['status']='pending'
            validated_data['level']=f'{int(level)+1}' if level <= 3 else level
        elif status=='pending':
            if level==0:
                validated_data['level']=1


        return super().update(instance, validated_data)



class UserIssueSerializers(serializers.ModelSerializer):

    ''' usermodel is related name of foreignkey'''
    issues = IssueSerializers(many = True)
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        usermodel = validated_data.pop('user')
        usermodel_instance = User.objects.create(**validated_data)
        for isue in usermodel:
            User.objects.create(user = usermodel_instance,**isue)
        return usermodel_instance





       # if level==1:
            #     level=2
            # elif level=='2':
            #     level=='3'
            # else:
            #     raise serializers.ValidationError('you can not forward')








        # instance.status_code = validated_data.get('Status_code',instance.status_code)
        # instance.module = validated_data.get('Module',instance.module)
        # instance.priority = validated_data.get('Priority',instance.priority)
        # instance.company_name = validated_data.get('compay name',instance.company_name)
        # instance.description = validated_data.get('description',instance.description)
        # instance.status = validated_data.get('status',instance.status)
        # instance.level = validated_data.get('level',instance.level)
        # instance.level= validated_data.get('level',instance.level)
        # instance.save()
    
    # def create(self, validated_data):
    #     x = super().create(validated_data)
    #     if x.level == 0:
    #         # level = x.level
    #         # level_issue= level+1
    #         # import ipdb;ipdb.set_trace()
    #         instance = Issue.objects.create(**validated_data)
    #         instance.save(level=validated_data[x.level+1])
    #         return instance
    #     else:
    #         return x


# class UserIssueSerializers(serializers.ModelSerializer):
    
#     # usermodel is related name of foreignkey
#     issues = IssueSerializers(many = True)
#     class Meta:
#         model = User
#         fields = '__all__'
#     def create(self, validated_data):
#         usermodel = validated_data.pop('user')
#         usermodel_instance = User.objects.create(**validated_data)
#         for isue in usermodel:
#             User.objects.create(user = usermodel_instance,**isue)
#         return usermodel_instance


    # user = serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())
    # issue_reporter= serializers.SerializerMethodField('_user')
    # def _user(self,obj):
    #     request = getattr(self.context,'request',None)
    #     if request:
    #         return request.user