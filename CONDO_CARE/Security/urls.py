from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'security'

urlpatterns = [

    path('dashboardsecurity/', views.dashboard_security, name='dashboardsecurity'),
    path('visitorregistration/', views.visitor_registration, name='visitorregistration'),
    path('visitorlog/', views.visitor_log, name='visitorlog'),
    path('viewvisitor/', views.view_visitor, name='viewvisitor'), 
    path('emergency/', views.security_emergency, name='emergency'),
    path('deletevisitor/<int:id>/', views.delete_visitor_tenant, name='delete_visitor_tenant'),
    path('delete/<int:id>/', views.delete_visitor, name='delete'),
    path('update/<int:id>/', views.update_visitor, name='update'),
    path('incidentreporting/', views.incident_reporting, name='incidentreporting'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
