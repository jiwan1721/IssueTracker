from dataclasses import fields
from pyexpat import model
from sys import settrace
from rest_framework import serializers
from django.contrib.auth.models import User


# from django.contrib.auth import get_user_model
# User = get_user_model()


# from . models import Issue
from . models import User,Issue
# from . forms import MyUserCreationForm,MyUserChangeForm

class IssueSerializers(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['user','status_code','module','priority','company_name','description']
    
        read_only_fields = ('is_active','is_staff')

    def create(self, validated_data):
        instance = Issue.objects.create(**validated_data)  # user=self.context['request'].user, 
        return instance

    def update(self, instance, validated_data):
        x =super().update(instance, validated_data)
        # import ipdb;ipdb.set_trace()
        return x


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username','first_name','last_name','company','mobile_number']
        fields = '__all__'
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class UserIssueSerializers(serializers.ModelSerializer):

    # usermodel is related name of foreignkey
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
    