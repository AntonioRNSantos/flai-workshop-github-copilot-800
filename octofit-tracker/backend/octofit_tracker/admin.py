from django.contrib import admin
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'team_id', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['created_at']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'activity_type', 'duration', 'calories', 'date', 'created_at']
    search_fields = ['user_id', 'activity_type']
    list_filter = ['activity_type', 'date', 'created_at']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['rank', 'user_name', 'team_name', 'total_calories', 'total_activities', 'updated_at']
    search_fields = ['user_name', 'team_name']
    list_filter = ['team_name', 'updated_at']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'difficulty', 'duration', 'calories_estimate', 'created_at']
    search_fields = ['name', 'description', 'category']
    list_filter = ['difficulty', 'category', 'created_at']
    ordering = ['-created_at']
