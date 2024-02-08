
from django.urls import path
from auth_app.views import *
urlpatterns = [
    path('signup/', hsignup, name='signup'),
    path('login/', hlogin, name='login'),
    path('logout/', hlogout, name='logout'),
]