from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('dashboardsecurity/', views.dashboard_security, name='dashboardsecurity'),
    path('visitorregistration/', views.visitor_registration, name='visitorregistration'),
    path('visitorlog/', views.visitor_log, name='visitorlog'),
     path('delete/<int:id>/', views.delete_visitor, name='delete'),
    path('incidentreporting/', views.incident_reporting, name='incidentreporting'),
    path('patrolreporting/', views.patrol_reporting, name='patrolreporting'),
    path('qr/', views.qr, name='qr'),
   
]
