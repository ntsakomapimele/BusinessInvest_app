from django.urls import path
from . import views

urlpatterns = [
    
     # path('', views.homepage, name = 'login-page' ), 
     path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name = 'dashboard'),
    # path('BusinessREG', views.business__view, name =  'business'),
    path('BusinessREG/', views.register_business, name='register_business'),
    path('registrations/', views.view_registrations, name='view_registrations'),
    path('business/<int:business_id>/',views.business_overview, name='investment_overview'),
    path('business_type/', views.business_type_list, name='business_type_list'),
    path('api/resources/', views.get_business_resources, name='get_business_resources'),
    path('business/<int:business_id>/apply-loan/', views.apply_for_loan, name='apply_loan'),
    path('loan/<int:loan_id>/status/', views.loan_status, name='loan_status'),
    path('business/<int:business_id>/loans/', views.my_loans, name='my_loans'),
]