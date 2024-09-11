from django.contrib import admin
from django.urls import path, include
from auth import views as auth_views

from .views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
     
    path("", home_view, name='home')
]
