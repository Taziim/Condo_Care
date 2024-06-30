from django.conf import settings
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'management'

urlpatterns = [
    path('maintenancerequestmanagement/', views.maintenance_request_management, name='maintenancerequestmanagement'),
    path('createbills/', views.create_bills, name='createbills'),
    path('dashboardmanagement/', views.dashboard_management, name='dashboardmanagement'),
    path('notificationannouncement/', views.notification_announcement, name='notificationannouncement'),
    path('createannouncement/', views.create_announcement, name='createannouncement'),
    path('announcementlog/', views.announcement_log, name='announcementlog'),
    path('notificationlog/', views.notification_log, name='notificationlog'),
    path('tenantbookinglist/', views.tenant_booking_list, name='tenant_booking_list'),
    path('managefacilities/', views.manage_facilities, name='managefacilities'),
    path('viewfacilities/', views.view_facilities, name='viewfacilities'),
    path('complainhistorytenant/', views.complain_history_tenant, name='complainhistorytenant'),
    
    path('deletehistorytenant/<int:id>/', views.delete_history_tenant, name='delete_history_tenant'),
    path('deleteallfacilities/', views.delete_all_facilities, name='delete_all_facilities'),
    path('deletetenantbooking/<int:id>/', views.delete_tenant_booking, name='delete_tenant_booking'),
    path('deletemaintenancerequest/<int:id>/', views.delete_maintenance_request, name='delete_maintenance_request'),
    path('updatemaintenancerequest/<int:id>/', views.update_maintenance_request, name='update_maintenance_request'),
    path('downloadimagemaintence/<int:id>/', views.download_image_maintence, name='download_image_maintence'),
    path('deleteannouncementlog/<int:id>/', views.delete_announcement_log, name='deleteannouncementlog'),
    path('deletenotificationlog/<int:notification_id>/', views.delete_notification_log, name='deletenotificationlog'),
    path('updateannouncement/<int:id>/', views.edit_announcement, name='updateannouncement'),
    path('editnotification/<int:notification_id>/', views.edit_notification, name='editnotification'),
    path('createnotification', views.create_notification, name='createnotification'),
    path('downloadimagecomplainhistory/<int:id>/', views.download_image_complainhistory, name='download_image_complainhistory'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)