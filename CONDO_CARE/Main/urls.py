from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.main, name='main'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.singup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),

]
