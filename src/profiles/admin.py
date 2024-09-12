from django.contrib import admin
from .models import CoachProfile, PlayerProfile

# Register your models here.
admin.site.register(CoachProfile)
admin.site.register(PlayerProfile)