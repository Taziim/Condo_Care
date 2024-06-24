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
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete_payment/<int:pdf_id>/', views.delete_payment, name='delete_payment'),
    path('download_pdf/<int:pdf_id>/', views.download_pdf, name='download_pdf'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)