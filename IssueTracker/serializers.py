from rest_framework import serializers

from . models import User,Issue
# from . forms import MyUserCreationForm,MyUserChangeForm

class IssueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['user','Reporting_person','status_code','modeule','priority','Company_name','Description']


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class UserCreationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUserCreationForm
#         fields = '__all__'