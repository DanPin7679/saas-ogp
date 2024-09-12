from django.db import models
from profiles.models import CoachProfile, PlayerProfile

class Meeting(models.Model):
    MEETING_TYPE_CHOICES = (
        ('inperson', 'In person'),
        ('virtual', 'Virtual'),
    )
    type = models.CharField(max_length=10, choices=MEETING_TYPE_CHOICES)
    date = models.DateField()
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE)
    player = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} on {self.date} | {self.coach.user.first_name} with {self.player.user.first_name}"