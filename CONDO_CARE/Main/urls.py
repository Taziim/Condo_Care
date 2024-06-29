from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.main, name='main'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.sing_up, name='signup'),

]
