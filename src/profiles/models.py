from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE)
        

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"