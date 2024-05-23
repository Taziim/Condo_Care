from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('maintenenecerequest/', views.maintenenece_request, name='maintenenecerequest'),
     path('requesthistory/', views.request_history, name='requesthistory'),
     path('bookfacilities/', views.book_facilities, name='bookfacilities'),
     path('availablefacilities/', views.available_facilities, name='availablefacilities'),
     path('bookinghistory/', views.booking_history, name='bookinghistory'),
     path('delete/<int:id>/', views.delete_history, name='delete'),
]