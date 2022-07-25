
from django.urls import path

from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('', index),
        #login
    path('login',login_request),
    path('register', register),
    path('logout', LogoutView.as_view(template_name='blogapp/logout.html'), name = 'Logout'),
    
        #url de blogapp
    path('contacto/', contacto),
    path('base', base),
        
]

