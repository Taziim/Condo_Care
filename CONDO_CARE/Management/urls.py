from django.urls import path
from . import views

urlpatterns = [
    path('maintenancerequestmanagement/', views.maintenance_request_management, name='maintenancerequestmanagement'),
    path('createbills/', views.create_bills, name='createbills'),
    path('dashboardmanagement/', views.dashboard_management, name='dashboardmanagement'),
    path('notificationannouncement/', views.notification_announcement, name='notificationannouncement'),
    path('createannouncement/', views.create_announcement, name='createannouncement'),
    path('announcementlog/', views.announcement_log, name='announcementlog'),
    path('notificationlog/', views.notification_log, name='notificationlog'),
    path('tenantbookinglist/', views.tenant_booking_list, name='tenant_booking_list'),
    path('managefacilities/', views.manage_facilities, name='manage_facilities'),


    
    # path('updatefacilities/<int:id>/', views.update_facilities, name='update_facilities'),
    path('deletetenantbooking/<int:id>/', views.delete_tenant_booking, name='delete_tenant_booking'),
    path('deletemaintenancerequest/<int:id>/', views.delete_maintenance_request, name='delete_maintenance_request'),
    path('updatemaintenancerequest/<int:id>/', views.update_maintenance_request, name='update_maintenance_request'),
    path('downloadimagemaintence/<int:id>/', views.download_image_maintence, name='download_image_maintence'),
    path('deleteannouncementlog/<int:id>/', views.delete_announcement_log, name='deleteannouncementlog'),
    path('deletenotificationlog/<int:notification_id>/', views.delete_notification_log, name='deletenotificationlog'),
    path('updateannouncement/<int:id>/', views.edit_announcement, name='updateannouncement'),
    path('editnotification/<int:notification_id>/', views.edit_notification, name='editnotification'),
    path('createnotification', views.create_notification, name='createnotification'),
]   