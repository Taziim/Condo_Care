from django.urls import path
from . import views

urlpatterns = [
    path('createbills/', views.create_bills, name='createbills'),
    path('dashboardmanagement/', views.dashboard_management, name='dashboardmanagement'),
    path('notificationannouncement/', views.notification_announcement, name='notificationannouncement'),
    path('createannouncement/', views.create_announcement, name='createannouncement'),
    path('announcementlog/', views.announcement_log, name='announcementlog'),
    path('deleteannouncementlog/<int:id>/', views.delete_announcement_log, name='deleteannouncementlog'),
]