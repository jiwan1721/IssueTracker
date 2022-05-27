from django.urls import path,include

from IssueTracker.serializers import UserIssueSerializers

from . import views
from . views import IssueView,UserView,UserIssueView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'bacic',IssueView)


urlpatterns = [

    # path('',include(router.urls)),

    path('index/',views.index,name = "hero"),
    path('basic/',IssueView.as_view(),name ='viewsets'),
    path('user/',UserView.as_view(),name = 'userView'),
    # path('uc/',userCreation.as_view(),name = 'uc')
    path('userIssue',UserIssueView.as_view(),name="userIssue"),

]