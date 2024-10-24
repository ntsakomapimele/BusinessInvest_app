from django.urls import path
from   . import views




urlpatterns = [
    
     # path('', views.homepage, name = 'login-page' ), 
     path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    
]