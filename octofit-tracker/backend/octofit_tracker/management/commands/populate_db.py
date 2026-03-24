
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
## Removed direct djongo import; use Django ORM only
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))

        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        ironman = User.objects.create_user(email='ironman@marvel.com', username='ironman', password='password', team_id=str(marvel.id))
        captainamerica = User.objects.create_user(email='captainamerica@marvel.com', username='captainamerica', password='password', team_id=str(marvel.id))
        batman = User.objects.create_user(email='batman@dc.com', username='batman', password='password', team_id=str(dc.id))
        superman = User.objects.create_user(email='superman@dc.com', username='superman', password='password', team_id=str(dc.id))

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user_id=str(ironman.id), activity_type='run', duration=30, calories_burned=300, date=date.today(), team_id=str(marvel.id))
        Activity.objects.create(user_id=str(captainamerica.id), activity_type='cycle', duration=45, calories_burned=400, date=date.today(), team_id=str(marvel.id))
        Activity.objects.create(user_id=str(batman.id), activity_type='swim', duration=60, calories_burned=500, date=date.today(), team_id=str(dc.id))
        Activity.objects.create(user_id=str(superman.id), activity_type='walk', duration=20, calories_burned=150, date=date.today(), team_id=str(dc.id))

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        workout1 = Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', suggested_for_ids=[str(ironman.id), str(captainamerica.id), str(batman.id), str(superman.id)])
        workout2 = Workout.objects.create(name='Strength Training', description='Strength for all heroes', suggested_for_ids=[str(ironman.id), str(captainamerica.id), str(batman.id), str(superman.id)])

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team_id=str(marvel.id), total_points=1900)
        Leaderboard.objects.create(team_id=str(dc.id), total_points=2050)


        self.stdout.write(self.style.SUCCESS('Unique index on email field is handled by Django User model constraints.'))

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
