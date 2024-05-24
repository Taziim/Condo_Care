from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('maintenenecerequest/', views.maintenenece_request, name='maintenenecerequest'),
     path('requesthistory/', views.request_history, name='requesthistory'),
     path('bookfacilities/', views.book_facilities, name='bookfacilities'),
     path('availablefacilities/', views.available_facilities, name='availablefacilities'),
     path('complain/', views.complain, name='complain'),
     path('bookinghistory/', views.booking_history, name='bookinghistory'),
     path('deletehistory/<int:id>/', views.delete_history, name='deletehistory'),
     path('updatehistory/<int:id>/', views.update_history, name='updatehistory'),
     
]