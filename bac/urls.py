from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('register/', views.register_bac, name='register_bac'),
    path('success/', lambda request: HttpResponse("تم التسجيل بنجاح!"), name='success'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update-status/<int:reg_id>/<str:new_status>/', views.update_status, name='update_status'),
    path('admit-card/', views.download_admit_card, name='admit_card'),
]


