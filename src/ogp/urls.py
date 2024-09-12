from django.contrib import admin
from django.urls import path, include
from auth import views as auth_views

from landing.views import landing_page


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
     
    path("", landing_page, name='home'),
    path('meetings/', include('meetings.urls')),
]
