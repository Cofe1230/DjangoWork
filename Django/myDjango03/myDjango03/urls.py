"""
URL configuration for myDjango03 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp03 import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.board_list),
    path('admin/', admin.site.urls),
    path('board_form/', views.board_form),
    path('board_insert/',views.board_insert),
    path('boards/',views.board_list),
    path('boards/<int:board_id>/', views.board_detail),
    path('login/', 
         auth_views.LoginView.as_view(template_name='common/login.html'),
         name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    
]
