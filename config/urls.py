"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from base import views 
from django.contrib.auth.views import LogoutView
from django.conf import settings  # 増えた
from django.conf.urls.static import static  # 増えた


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Account
    path('logout/',LogoutView.as_view()),
    path('login/',views.Login.as_view()),
    path('signup/',views.SignupView.as_view()),
    
    #User
    path('user/<str:pk>/',views.UserListView.as_view()),
    path('user/good/<str:pk>/',views.GoodView.as_view()),
    path('user/like/<str:pk>/',views.LikeView.as_view()),
    path('profile/',views.ProfileUpdateView.as_view()),
    path('account/',views.AccountUpdateView.as_view()),
    
    
    #Item
    path('item/delete/<str:pk>/',views.ItemDeleteView.as_view()),
    path('item/update/<str:pk>/',views.ItemUpdateView.as_view()),
    path('item/create/',views.ItemCreateView.as_view()),
    path('item/<str:pk>/',views.detailfunc),
    path('item/good/<str:pk>/',views.goodfunc),
    
    
    path('',views.ItemListView.as_view()),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
