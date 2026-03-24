from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields can be added here
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('User', related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Duration in minutes')
    calories_burned = models.FloatField()
    date = models.DateField()
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='activities')

class Leaderboard(models.Model):
    team = models.OneToOneField('Team', on_delete=models.CASCADE, related_name='leaderboard')
    total_points = models.IntegerField(default=0)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField('User', related_name='suggested_workouts')
    created_at = models.DateTimeField(auto_now_add=True)
