from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('addtenant1/', views.add_tenant1, name='addtenant1'),
    path('addtenant2/', views.add_tenant2, name='addtenant2'),
    path('addtenant3/', views.add_tenant3, name='addtenant3'),
    path('viewtenantinfo/', views.view_tenant_info, name='viewtenantinfo'),
    path('viewtenantagree/', views.view_tenant_agree, name='viewtenantagree'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('download/passport-or-nric/<int:id>/', views.download_passport_or_nric, name='download_passport_or_nric'),
    path('download/driving-license/<int:id>/', views.download_driving_license, name='download_driving_license'),


]