from users_app import views
from django.urls import path,include # type: ignore
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('register', views.register, name='register'),
    # path('login', auth_views.LoginView.as_view(template_name='login.html '), name='login'),
    # path('logout', TemplateView.as_view(template_name='logout.html'), name='logout'), 
    path('logout', views.logout_view, name="logout")
    
    
    
    
    
    ]