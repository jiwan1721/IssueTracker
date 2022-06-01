
from rest_framework import serializers
from traitlets import default
from . models import LEVEL, User,Issue


class IssueSerializers(serializers.ModelSerializer):
    # level=serializers.ChoiceField(choices=LEVEL,default='1')

    class Meta:
        model = Issue
        fields = ['id','status_code','module','priority','company_name','description','status']
    
        read_only_fields = ('is_active','is_staff')

    def create(self, validated_data):
        validated_data['level']='1'
        # validated_data['recipent']=self.name
        return super().create(validated_data)
    def update(self, instance, validated_data):
        # import ipdb;ipdb.set_trace()

        #     instance.level = '0'
        #     instance.status = 'solved'
           
        #     instance.save()

        instance.status_code = validated_data.get('Status_code',instance.status_code)
        instance.module = validated_data.get('Module',instance.module)
        instance.priority = validated_data.get('Priority',instance.priority)
        instance.company_name = validated_data.get('compay name',instance.company_name)
        instance.description = validated_data.get('description',instance.description)
        instance.status = validated_data.get('status',instance.status)
        instance.level = validated_data.get('level',instance.level)
        
        instance.level= validated_data.get('level',instance.level)
        instance.save()

  
        return instance


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username','first_name','last_name','company','mobile_number']
        fields = '__all__'
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)


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
    