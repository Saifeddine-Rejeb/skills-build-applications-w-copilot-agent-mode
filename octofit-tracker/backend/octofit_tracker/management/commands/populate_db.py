from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many([
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ])

        db.teams.insert_one({"_id": ObjectId(), "name": "Blue Team", "members": ["thundergod", "metalgeek", "zerocool", "crashoverride", "sleeptoken"]})

        db.activity.insert_many([
            {"_id": ObjectId(), "user": "thundergod", "activity_type": "Cycling", "duration": 60},
            {"_id": ObjectId(), "user": "metalgeek", "activity_type": "Crossfit", "duration": 120},
            {"_id": ObjectId(), "user": "zerocool", "activity_type": "Running", "duration": 90},
            {"_id": ObjectId(), "user": "crashoverride", "activity_type": "Strength", "duration": 30},
            {"_id": ObjectId(), "user": "sleeptoken", "activity_type": "Swimming", "duration": 75},
        ])

        db.leaderboard.insert_many([
            {"_id": ObjectId(), "user": "thundergod", "score": 100},
            {"_id": ObjectId(), "user": "metalgeek", "score": 90},
            {"_id": ObjectId(), "user": "zerocool", "score": 95},
            {"_id": ObjectId(), "user": "crashoverride", "score": 85},
            {"_id": ObjectId(), "user": "sleeptoken", "score": 80},
        ])

        db.workouts.insert_many([
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
