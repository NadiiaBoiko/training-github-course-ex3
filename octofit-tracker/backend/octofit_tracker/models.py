from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    team_id = models.CharField(max_length=50, null=True, blank=True, help_text='MongoDB ObjectId of the team')

class Team(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user_id = models.CharField(max_length=50, help_text='MongoDB ObjectId of the user')
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Duration in minutes')
    calories_burned = models.FloatField()
    date = models.DateField()
    team_id = models.CharField(max_length=50, null=True, blank=True, help_text='MongoDB ObjectId of the team')

class Leaderboard(models.Model):
    team_id = models.CharField(max_length=50, help_text='MongoDB ObjectId of the team')
    total_points = models.IntegerField(default=0)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for_ids = models.JSONField(default=list, help_text='List of User ObjectIds')
    created_at = models.DateTimeField(auto_now_add=True)
