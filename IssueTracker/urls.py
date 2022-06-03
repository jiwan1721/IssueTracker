from django.urls import path,include

from IssueTracker.serializers import UserIssueSerializers
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import IssueView,UserView,UserIssueView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user',views.UserView,basename='user')
router.register(r'Assigned_issues',views.IssueView,basename='issues')
router.register(r'admin-user',views.AdminViewSet,basename='for admin only')
router.register(r'user-Specific-Issue',views.UserZero,basename='userIssue')


urlpatterns = [
    path('',include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)














    # path('issues/',IssueView.as_view(),name ='issues'),s
    # path('issues/assigned/',assignedIssue.as_view(),name="assignedIssues"),

    # path('user/',UserView.as_view(),name = 'users'),
    # path('uc/',userCreation.as_view(),name = 'uc')
    # path('nestedissues/',UserIssueView.as_view(),name="userIssue"),
    # path('user/<int:pk>/',serializerIssue,name = 'funcUser')