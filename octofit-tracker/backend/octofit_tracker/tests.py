from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone


class TeamModelTest(TestCase):
    """Test the Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='Test Description',
            created_at=timezone.now()
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'Test Description')
        self.assertIsNotNone(self.team._id)
    
    def test_team_string_representation(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), 'Test Team')


class UserModelTest(TestCase):
    """Test the User model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='Test Description',
            created_at=timezone.now()
        )
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            team_id=str(self.team._id),
            created_at=timezone.now()
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team_id, str(self.team._id))
        self.assertIsNotNone(self.user._id)
    
    def test_user_string_representation(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), 'Test User')


class ActivityModelTest(TestCase):
    """Test the Activity model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            created_at=timezone.now()
        )
        self.activity = Activity.objects.create(
            user_id=str(self.user._id),
            activity_type='Running',
            duration=30,
            calories=300,
            date=timezone.now(),
            created_at=timezone.now()
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)
        self.assertIsNotNone(self.activity._id)
    
    def test_activity_string_representation(self):
        """Test the string representation of an activity"""
        self.assertEqual(str(self.activity), 'Running - 30 mins')


class WorkoutModelTest(TestCase):
    """Test the Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='Test Description',
            difficulty='Medium',
            duration=45,
            calories_estimate=400,
            category='Cardio',
            created_at=timezone.now()
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.difficulty, 'Medium')
        self.assertEqual(self.workout.duration, 45)
        self.assertEqual(self.workout.calories_estimate, 400)
        self.assertIsNotNone(self.workout._id)
    
    def test_workout_string_representation(self):
        """Test the string representation of a workout"""
        self.assertEqual(str(self.workout), 'Test Workout')


class APIEndpointTests(APITestCase):
    """Test the API endpoints"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='Test Description',
            created_at=timezone.now()
        )
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            team_id=str(self.team._id),
            created_at=timezone.now()
        )
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='Test Description',
            difficulty='Medium',
            duration=45,
            calories_estimate=400,
            category='Cardio',
            created_at=timezone.now()
        )
    
    def test_api_root(self):
        """Test that the API root endpoint is accessible"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
    
    def test_teams_list(self):
        """Test that the teams list endpoint is accessible"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_users_list(self):
        """Test that the users list endpoint is accessible"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_workouts_list(self):
        """Test that the workouts list endpoint is accessible"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_activities_list(self):
        """Test that the activities list endpoint is accessible"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_leaderboard_list(self):
        """Test that the leaderboard list endpoint is accessible"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
