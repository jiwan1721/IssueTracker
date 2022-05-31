from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser



LEVEL = (
    (0,'level zero'),
    (1,'Level one'),
    (2,'Level two'),
    (3,'Level three'),
)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20,unique=True)
    company = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=10, unique=True)
    level = models.CharField(choices=LEVEL,max_length=20)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
        # return "user  name = %s,Company name = %s"%(self.name,self.company)
    


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

    level = models.CharField(max_length=20,choices=LEVEL,default='L0')
    recipent = models.ForeignKey(User,related_name = 'issues',on_delete = models.CASCADE)
    status_code = models.CharField(choices=STATUS_CODE,max_length=30,default='other')
    module = models.CharField(choices = MODULE,max_length =30,default='other')
    priority = models.CharField(choices = PRIORITY,max_length=30,default='low')
    company_name = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS,max_length=20,default='pending')
    
    class Meta:
        permissions = (
            ('view_Issue','can see issue'),
            ('report_issue','user can report issue'),
            ('forward_issue','user can forwad isuue to senior level'),
            ('solve_Issue','can solve Issue'),
        )
    def __str__(self):
        return " Issue priority:  %s, status code:  %s, " % (self.status,self.status_code)














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