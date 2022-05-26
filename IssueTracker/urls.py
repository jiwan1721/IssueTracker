from django.urls import path,include

from . import views
from . views import IssueView,UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('',views.index,name = "hero"),
    path('basic/',IssueView.as_view(),name ='viewsets'),
    path('user/',UserView.as_view(),name = 'userView'),
    # path('uc/',userCreation.as_view(),name = 'uc')

]