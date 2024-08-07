from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tenant'

urlpatterns = [
    
     path('dashboardtenant/', views.dashboard_tenant, name='dashboardtenant'),
     path('maintenenecerequest/', views.maintenenece_request, name='maintenenecerequest'),
     path('requesthistory/', views.request_history, name='requesthistory'),
     path('bookfacilities/', views.book_facilities, name='bookfacilities'),
     path('availablefacilities/', views.available_facilities, name='availablefacilities'),
     path('complain/', views.make_complaint, name='complain'),
     path('complainhistory/', views.complain_history, name='complainhistory'),
     path('bookinghistory/', views.booking_history, name='bookinghistory'),
     path('createvisitor/', views.create_visitor, name='createvisitor'), 
     path('viewannouncement/', views.view_announcement, name='viewannouncement'), 

     path('deleterequest/<int:id>/', views.delete_request, name='delete_request'), 
     path('deletehistory/<int:id>/', views.delete_history, name='deletehistory'),
     path('deletecomplianhistory/<int:id>/', views.delete_complain_history, name='deletecomplianhistory'),
     path('updatehistory/<int:id>/', views.update_history, name='updatehistory'),
     path('deleteannouncement/<int:id>/', views.delete_announcement, name='delete_announcement'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
