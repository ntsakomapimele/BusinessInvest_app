# FNBProj/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication URLs
    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_view, name='register'),
    
    # Business URLs
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('BusinessREG/', views.register_business, name='register_business'),
    path('registrations/', views.view_registrations, name='view_registrations'),
    path('business/<int:business_id>/', views.business_overview, name='business_overview'),  # Updated name
    path('business_type/', views.business_type_list, name='business_type_list'),
    path('api/resources/', views.get_business_resources, name='get_business_resources'),
    
    # Loan URLs
    path('business/<int:business_id>/apply-loan/', views.apply_for_loan, name='apply_loan'),
    path('loan/<int:loan_id>/status/', views.loan_status, name='loan_status'),
    path('business/<int:business_id>/loans/', views.my_loans, name='my_loans'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)