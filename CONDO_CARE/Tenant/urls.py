from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('maintenenecerequest/', views.maintenenece_request, name='maintenenecerequest'),
     path('requesthistory/', views.request_history, name='requesthistory'),
    # path('addtenant3/', views.add_tenant3, name='addtenant3'),
    # path('viewtenantinfo/', views.view_tenant_info, name='viewtenantinfo'),
    # path('viewtenantagree/', views.view_tenant_agree, name='viewtenantagree'),
    # path('delete/<int:id>/', views.delete, name='delete'),
    # path('download/passport-or-nric/<int:id>/', views.download_passport_or_nric, name='download_passport_or_nric'),
    # path('download/driving-license/<int:id>/', views.download_driving_license, name='download_driving_license'),


]