from django.urls import path
from .views import Signup,CustomLogoutView,myaccount
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('signup/',Signup.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name ='userprofile/login.html'),name='login'),
    #path('logout/', LogoutView.as_view(), name='logout').
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('account/',myaccount,name='myaccount')
    
  
]
