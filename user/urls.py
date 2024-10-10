from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('user', views.user, name="user"),
    path('user_details/', views.user_details, name='user_details'),
    path('contract_fines/<int:contract_id>/', views.contract_fines, name='contract_fines'),
    path('driver/', views.driver, name="driver"),
    path('driver_dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('contract_condition_report/<int:contract_id>/', views.contract_condition_report, name='contract_condition_report'),
    
]
