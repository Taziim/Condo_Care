from django.urls import path
from . import views

urlpatterns = [
    path('createbills/', views.create_bills, name='createbills'),
]
