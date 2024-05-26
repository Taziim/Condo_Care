from django.urls import path
from . import views

urlpatterns = [

    path('main/', views.main, name='main'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.sing_up, name='signup'), 
]
