from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboardowner/', views.dashboard_owner, name='dashboardowner'),
    path('addtenant1/', views.add_tenant1, name='addtenant1'),
    path('addtenant2/', views.add_tenant2, name='addtenant2'),
    path('addtenant3/', views.add_tenant3, name='addtenant3'),
    path('viewtenantinfo/', views.view_tenant_info, name='viewtenantinfo'),
    path('viewtenantagree/', views.view_tenant_agree, name='viewtenantagree'),
    path('viewpayment/', views.view_payment, name='viewpayment'),
    path('community/', views.community, name='community'),
    path('createannouncementowner/', views.create_announcement_owner, name='createannouncementowner'),
    path('announcementlogowner/', views.announcement_log_owner, name='announcementlogowner'),



    path('delete_info/<int:id>/', views.delete_info, name='delete_info'),
    path('delete_agree/<int:id>/', views.delete_agree, name='delete_agree'),
    path('delete_payment/<int:pdf_id>/', views.delete_payment, name='delete_payment'),
    path('download_pdf/<int:pdf_id>/', views.download_pdf, name='download_pdf'),
    path('download_passport_or_nric/<int:id>/', views.download_passport_or_nric, name='download_passport_or_nric'),
    path('download_driving_license/<int:id>/', views.download_driving_license, name='download_driving_license'),
    path('like/<int:message_id>/', views.like_message, name='like_message'),
    path('unlike/<int:message_id>/', views.unlike_message, name='unlike_message'),
    path('postmessage/', views.post_message, name='post_message'),
    path('deletemessage/<int:id>/', views.delete_message, name='delete_message'),
    path('viewmessage/', views.view_message, name='view_message'),
    path('deleteannouncementlogowner/<int:id>/', views.delete_announcement_log, name='delete_announcement_log'),
    path('updateannouncementowner/<int:id>/', views.update_announcement_owner, name='update_announcement_owner'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)