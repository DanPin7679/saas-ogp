import random
from faker import Faker
from django.core.management.base import BaseCommand
from meetings.models import Meeting
from profiles.models import CoachProfile, PlayerProfile

class Command(BaseCommand):
    help = "Generates meetings for testing"

    def handle(self, *args, **options):
        fake = Faker()
        coach = CoachProfile.objects.filter(id=1).first()
        print(coach)
        player = PlayerProfile.objects.filter(id=1).first()
        types = [x[0] for x in Meeting.MEETING_TYPE_CHOICES]
        for i in range(20):
            Meeting.objects.create(
                date=fake.date_between(start_date='-1y', end_date='today'),
                type=random.choice(types),
                coach=coach,
                player=player
            )