
from rest_framework import serializers
from . models import LEVEL, User,Issue


class IssueSerializers(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['recipent','id','level','status_code','module','priority','company_name','description','status']
    
        read_only_fields = ('is_active','is_staff')
    
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












# def create(self, validated_data):
#     instance = Issue.objects.create(**validata) ed_dat # user=self.context['request'].user, 
#     return instance

# def update(self, instance, validated_data):
#     x =super().update(instance, validated_data)
#     # import ipdb;ipdb.set_trace()
#     return x


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
    