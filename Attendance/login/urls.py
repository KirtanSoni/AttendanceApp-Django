
from django.urls import path
from login.views import login, auth_view, logout, loggedin, invalidlogin, signup 
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('',login,name='login'),
    path('auth/',auth_view,name='auth'),
    path('logout/',logout,name='logout'),
    path('loggedin/',loggedin,name='loggedin'),
    path('invalidlogin/',invalidlogin,name='invalidlogin'),
    path('signup/',signup,name='signup'),
 
]
   
