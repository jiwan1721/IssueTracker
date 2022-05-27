from django.db import models
from django.contrib.auth.models import AbstractUser





class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
class User_Types(BaseModel):
    USER_LEVEL = (
        ('L0','normal user'),
        ('L1','Level one'),
        ('L2','Level two'),
        ('L3','Level three'),
    )


    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20,unique=True)
    company = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=10, unique=True)
    user_level = models.CharField(choices=USER_LEVEL,max_length=20)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']

    def __str__(self):
        return "user  name = %s,Company name = %s"%(self.name,self.company)
    


class Issue(BaseModel):
    PRIORITY = (
        ('high','HIGH'),
        ('medium','MEDIUM'),
        ('low','LOW')
    )
    STATUS = (
        ('pending','Pending'),
        ('solved','Solved'),
        ('forward','forward'),
    )
    MODULE = (
        ('attendence','Attendence'),
        ('payroll','PayRoll'),
        ('leave','Leave'),
        ('calender','Calender'),
        ('worklog','Worklog'),
        ('other','Other'),
    )
    STATUS_CODE = (
        ('404','404'),
        ('304','404'),
        ('500','500'),
        ('501','500'),
        ('502','502'),
        ('other','Other'),
    )

    user = models.ForeignKey(User_Types,related_name = 'usermodel',on_delete = models.CASCADE,null = True)
    # recipent = models.ForeignKey(User_Types,related_name='userlevel',on_delete=models.CASCADE,null=True)
    status_code = models.CharField(choices=STATUS_CODE,max_length=30,default='other')
    module = models.CharField(choices = MODULE,max_length =30,default='other')
    priority = models.CharField(choices = PRIORITY,max_length=30)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices=STATUS,max_length=20,default='pending')
    
    class Meta:
        permissions = (
            ('view_Issue','can see issue'),
            ('report_issue','user can report issue'),
            ('forward_issue','user can forwad isuue to senior level'),
            ('solve_Issue','can solve Issue'),
        )


    def __str__(self):

        return "user name:  %s, Issue priority:  %s, status code:  %s, " % (self.reporting_person,self.status,self.status_code)


        # return self.reporting_person+self.status













# class Users(AbstractUser):
#     GENDER_CHOICES = (
#         ('MALE','Male'),
#         ('Female','Female'),
#     )
#     USER_GROUPS = (
#         ('NORMAL_USER','Normal_user'),
#         ('LEVEL_ONE_SUPPORT','level_one_support'),
#         ('LEVEL_TWO_SUPPORT','level_two_support'),
#         ('LEVEL_THREE_SUPPORT','level_three_support'),
#     )
#     name = models.CharField(max_length=30,unique=True)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=15,choices = GENDER_CHOICES,blank=True,null = True)












# Create your models here.


# class User(AbstractUser):
#     username = models.CharField(max_length=56,blank=True,null=True,unique=True)
#     email = models.EmailField('email address',unique=True)
#     phone_no = models.CharField(max_length=10)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#     def __str__(self):
#         return "{}".format(self.email)