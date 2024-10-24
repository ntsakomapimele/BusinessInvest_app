from django.urls import path
from   . import views





urlpatterns = [
    
     # path('', views.homepage, name = 'login-page' ), 
     path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard', views.dashboard_view, name = 'dashboard'),
    # path('BusinessREG', views.business__view, name =  'business'),
    path('BusinessREG/', views.register_business, name='register_business'),
    path('registrations/', views.view_registrations, name='view_registrations'),

    
]