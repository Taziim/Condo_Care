from django.urls import path
from . import views

urlpatterns = [
    path('createbills/', views.create_bills, name='createbills'),
    path('dashboardmanagement/', views.dashboard_management, name='dashboardmanagement'),
    path('notificationannouncement/', views.notification_announcement, name='notificationannouncement'),
    path('createannouncement/', views.create_announcement, name='createannouncement'),
    path('announcementlog/', views.announcement_log, name='announcementlog'),
    path('notificationlog/', views.notification_log, name='notificationlog'),
    path('deleteannouncementlog/<int:id>/', views.delete_announcement_log, name='deleteannouncementlog'),
    path('deletenotificationlog/<int:notification_id>/', views.delete_notification_log, name='deletenotificationlog'),
    path('updateannouncement/<int:id>/', views.edit_announcement, name='updateannouncement'),
    path('editnotification/<int:notification_id>/', views.edit_notification, name='editnotification'),
    path('createnotification', views.create_notification, name='createnotification'),
]   