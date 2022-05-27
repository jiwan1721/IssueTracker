from dataclasses import fields
from pyexpat import model
from sys import settrace
from rest_framework import serializers


from . models import User_Types,Issue
# from . forms import MyUserCreationForm,MyUserChangeForm

class IssueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['status_code','module','priority','company_name','description']

    def create(self, validated_data):
        instance = Issue.objects.create(user=self.context['request'].user, **validated_data)
        return instance

    def update(self, instance, validated_data):
        x =super().update(instance, validated_data)
        # import ipdb;ipdb.set_trace()
        return x


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User_Types
        fields = '__all__'


class UserIssueSerializers(serializers.ModelSerializer):

    # usermodel is related name of foreignkey
    issues = IssueSerializers(many = True)
    class Meta:
        model = User_Types
        fields = '__all__'
    def create(self, validated_data):
        usermodel = validated_data.pop('usermodel')
        usermodel_instance = User_Types.objects.create(**validated_data)
        for isue in usermodel:
            User_Types.objects.create(user = usermodel_instance,**isue)
        return super().create(validated_data)