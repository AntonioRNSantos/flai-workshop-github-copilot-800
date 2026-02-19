from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
import random
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        
        # Delete existing data using Django ORM
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared.'))
        
        # Create Teams
        self.stdout.write(self.style.WARNING('Creating teams...'))
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes',
            created_at=timezone.now()
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League Members',
            created_at=timezone.now()
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))
        
        # Create Users - Marvel Heroes
        self.stdout.write(self.style.WARNING('Creating Marvel heroes...'))
        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'tony.stark@marvel.com'},
            {'name': 'Captain America', 'email': 'steve.rogers@marvel.com'},
            {'name': 'Thor', 'email': 'thor.odinson@marvel.com'},
            {'name': 'Black Widow', 'email': 'natasha.romanoff@marvel.com'},
            {'name': 'Hulk', 'email': 'bruce.banner@marvel.com'},
            {'name': 'Spider-Man', 'email': 'peter.parker@marvel.com'},
            {'name': 'Black Panther', 'email': 'tchalla@marvel.com'},
            {'name': 'Doctor Strange', 'email': 'stephen.strange@marvel.com'},
        ]
        
        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team_id=str(team_marvel._id),
                created_at=timezone.now()
            )
            marvel_users.append(user)
        
        # Create Users - DC Heroes
        self.stdout.write(self.style.WARNING('Creating DC heroes...'))
        dc_heroes = [
            {'name': 'Superman', 'email': 'clark.kent@dc.com'},
            {'name': 'Batman', 'email': 'bruce.wayne@dc.com'},
            {'name': 'Wonder Woman', 'email': 'diana.prince@dc.com'},
            {'name': 'The Flash', 'email': 'barry.allen@dc.com'},
            {'name': 'Aquaman', 'email': 'arthur.curry@dc.com'},
            {'name': 'Green Lantern', 'email': 'hal.jordan@dc.com'},
            {'name': 'Cyborg', 'email': 'victor.stone@dc.com'},
            {'name': 'Shazam', 'email': 'billy.batson@dc.com'},
        ]
        
        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team_id=str(team_dc._id),
                created_at=timezone.now()
            )
            dc_users.append(user)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(marvel_users) + len(dc_users)} users'))
        
        # Create Activities
        self.stdout.write(self.style.WARNING('Creating activities...'))
        activity_types = [
            {'type': 'Running', 'calories_per_min': 10},
            {'type': 'Cycling', 'calories_per_min': 8},
            {'type': 'Swimming', 'calories_per_min': 12},
            {'type': 'Weight Training', 'calories_per_min': 7},
            {'type': 'Yoga', 'calories_per_min': 4},
            {'type': 'Boxing', 'calories_per_min': 11},
            {'type': 'CrossFit', 'calories_per_min': 13},
            {'type': 'Hiking', 'calories_per_min': 6},
        ]
        
        all_users = marvel_users + dc_users
        activities_count = 0
        
        for user in all_users:
            # Create 5-10 random activities for each user
            num_activities = random.randint(5, 10)
            for _ in range(num_activities):
                activity_data = random.choice(activity_types)
                duration = random.randint(20, 120)  # 20-120 minutes
                calories = duration * activity_data['calories_per_min']
                days_ago = random.randint(0, 30)
                
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=activity_data['type'],
                    duration=duration,
                    calories=calories,
                    date=timezone.now() - timedelta(days=days_ago),
                    created_at=timezone.now()
                )
                activities_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activities_count} activities'))
        
        # Create Leaderboard entries
        self.stdout.write(self.style.WARNING('Creating leaderboard entries...'))
        leaderboard_entries = []
        
        for user in all_users:
            # Calculate total calories and activities for each user
            user_activities = Activity.objects.filter(user_id=str(user._id))
            total_calories = sum(activity.calories for activity in user_activities)
            total_activities = user_activities.count()
            
            leaderboard_entries.append({
                'user': user,
                'total_calories': total_calories,
                'total_activities': total_activities
            })
        
        # Sort by total calories descending
        leaderboard_entries.sort(key=lambda x: x['total_calories'], reverse=True)
        
        # Create leaderboard records with ranks
        for rank, entry in enumerate(leaderboard_entries, start=1):
            user = entry['user']
            team_name = team_marvel.name if user.team_id == str(team_marvel._id) else team_dc.name
            
            Leaderboard.objects.create(
                user_id=str(user._id),
                user_name=user.name,
                team_id=user.team_id,
                team_name=team_name,
                total_calories=entry['total_calories'],
                total_activities=entry['total_activities'],
                rank=rank,
                updated_at=timezone.now()
            )
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(leaderboard_entries)} leaderboard entries'))
        
        # Create Workouts
        self.stdout.write(self.style.WARNING('Creating workout suggestions...'))
        workouts = [
            {
                'name': 'Super Soldier Sprint',
                'description': 'High-intensity interval training inspired by Captain America\'s training regimen',
                'difficulty': 'Hard',
                'duration': 45,
                'calories_estimate': 500,
                'category': 'Cardio'
            },
            {
                'name': 'Asgardian Strength Circuit',
                'description': 'Thor-inspired strength training with hammer swings and power movements',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_estimate': 600,
                'category': 'Strength'
            },
            {
                'name': 'Spider Agility Workout',
                'description': 'Agility and flexibility training like Spider-Man\'s acrobatics',
                'difficulty': 'Medium',
                'duration': 40,
                'calories_estimate': 400,
                'category': 'Agility'
            },
            {
                'name': 'Bat Cave Core Training',
                'description': 'Batman\'s core strengthening routine for ultimate stability',
                'difficulty': 'Medium',
                'duration': 30,
                'calories_estimate': 300,
                'category': 'Core'
            },
            {
                'name': 'Amazonian Warrior Workout',
                'description': 'Wonder Woman\'s full-body warrior training program',
                'difficulty': 'Hard',
                'duration': 55,
                'calories_estimate': 550,
                'category': 'Full Body'
            },
            {
                'name': 'Flash Speed Training',
                'description': 'Lightning-fast cardio and speed work inspired by The Flash',
                'difficulty': 'Hard',
                'duration': 35,
                'calories_estimate': 450,
                'category': 'Cardio'
            },
            {
                'name': 'Mystic Arts Meditation',
                'description': 'Doctor Strange\'s mindfulness and flexibility routine',
                'difficulty': 'Easy',
                'duration': 25,
                'calories_estimate': 150,
                'category': 'Flexibility'
            },
            {
                'name': 'Kryptonian Power Lift',
                'description': 'Superman\'s strength training for maximum power',
                'difficulty': 'Hard',
                'duration': 50,
                'calories_estimate': 500,
                'category': 'Strength'
            },
            {
                'name': 'Atlantean Swimming Session',
                'description': 'Aquaman\'s underwater-inspired swimming workout',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 450,
                'category': 'Cardio'
            },
            {
                'name': 'Wakandan Warrior Dance',
                'description': 'Black Panther\'s cultural combat dance and conditioning',
                'difficulty': 'Medium',
                'duration': 40,
                'calories_estimate': 350,
                'category': 'Cardio'
            },
            {
                'name': 'Arc Reactor Recovery',
                'description': 'Iron Man\'s low-impact recovery and mobility routine',
                'difficulty': 'Easy',
                'duration': 30,
                'calories_estimate': 200,
                'category': 'Recovery'
            },
            {
                'name': 'Green Lantern Willpower Training',
                'description': 'Mental focus and endurance training inspired by the Green Lantern Corps',
                'difficulty': 'Medium',
                'duration': 35,
                'calories_estimate': 300,
                'category': 'Endurance'
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(
                name=workout_data['name'],
                description=workout_data['description'],
                difficulty=workout_data['difficulty'],
                duration=workout_data['duration'],
                calories_estimate=workout_data['calories_estimate'],
                category=workout_data['category'],
                created_at=timezone.now()
            )
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workouts'))
        
        # Create unique index on email field for users collection
        self.stdout.write(self.style.WARNING('Creating unique index on users.email...'))
        try:
            client = MongoClient('localhost', 27017)
            db = client['octofit_db']
            db.users.create_index([('email', 1)], unique=True)
            self.stdout.write(self.style.SUCCESS('Unique index created on users.email'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Index may already exist: {e}'))
        
        self.stdout.write(self.style.SUCCESS('\n=== Database population completed successfully! ==='))
        self.stdout.write(self.style.SUCCESS(f'Teams: 2'))
        self.stdout.write(self.style.SUCCESS(f'Users: {len(all_users)}'))
        self.stdout.write(self.style.SUCCESS(f'Activities: {activities_count}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard Entries: {len(leaderboard_entries)}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts: {len(workouts)}'))
