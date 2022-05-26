from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class User(AbstractUser):
#     username = models.CharField(max_length=56,blank=True,null=True,unique=True)
#     email = models.EmailField('email address',unique=True)
#     phone_no = models.CharField(max_length=10)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#     def __str__(self):
#         return "{}".format(self.email)
    
class User(AbstractUser):
    USER_LEVEL = (
        ('L0','normal user'),
        ('L1','Level one'),
        ('L2','Level two'),
        ('L3','Level three'),
    )


    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    Company = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=10, unique=True)
    user_level = models.CharField(choices=USER_LEVEL,max_length=20)

    def __str__(self):
        return self.name
    


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

class Issue(models.Model):
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

    user = models.ForeignKey(User,related_name = 'usermodel',on_delete = models.CASCADE,null = True)
    Reporting_person = models.CharField(max_length=100)
    status_code = models.IntegerField()
    module = models.CharField(max_length=100)
    priority = models.CharField(choices = PRIORITY,max_length=30)
    Company_name = models.CharField(max_length=100)
    Description = models.TextField()
    status = models.CharField(choices=STATUS,max_length=20)
    
    class Meta:
        permissions = (
            ('view_Issue','can see issue'),
            ('report_issue','user can report issue'),
            ('forward_issue','user can forwad isuue to senior level'),
            ('solve_Issue','can solve Issue'),
        )


    def __str__(self):
        return self.Reporting_person


