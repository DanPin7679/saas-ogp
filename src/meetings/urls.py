from django.urls import path
from meetings import views


urlpatterns = [
    path("", views.meetings_page, name='meetings'),
    path("calendar/", views.meetings_list, name='meetings-list')
]