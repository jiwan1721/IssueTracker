from rest_framework.test import APIRequestFactory, force_authenticate,APIClient,APITestCase
from IssueTracker.models import User
from IssueTracker.views import UserView
from django.test import Client
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.test import Client

# "detail": "Authentication credentials were not provided."
# /api-auth/login/?next=/


class TestAbc(APITestCase):
    # @property
    # def userUrl():
    #     return reverse('Issue:user')
    # def setUp(self):
    #     self.client.bulk_create([
    #         Client.create(username=f'jiwan{i}',level=i,mobile_number=f'986629030{i}',email=f'jiwan{i}@gmail.com')
    #         for i in range(0,3)          
    #     ])
    def test_ABC(self):
        # factory = APIRequestFactory()
        # user = User.objects.get(username='admin')
        # view = UserView
        # token = Token.objects.get(user__username='admin')
        # client = APIClient()
        user = User.objects.create(username='testuser',is_staff=True,is_active='True')
        user.set_password('12345')
        user.save()

        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        print(logged_in)
                
        # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        data = {
            'id' :'46',
            'username':'hariparsad',
            'first_name':'hariparsad',
            'name':'hariparsad',
            'email':'hariparsad@gmail.com',
            'company':'aayulogic',
            'level':'1',
            'mobile_number':98663820300
        }
        response = c.get('/admin-user/')
        print(response)
        self.assertEqual(response.name,3)

# response=view(request)



# class userTestCAse(unittest.TestCase):
    # def setUp(self):
    #     self.client= Client()
    
    # def test_user(self):
    #     client= Client()
    #     response= client.get('/user',format =json)
    #     self.assertEqual(response.status_code,200)