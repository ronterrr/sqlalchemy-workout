#!/usr/bin/env python3

from datetime import date
from app import app
from models import *

with app.app_context():
    print("Clearing existing data...")

    WorkoutExercise.query.delete()
    Exercise.query.delete()
    Workout.query.delete()
    db.session.commit()

    print("Seeding exercises...")
    push_up = Exercise(
        name="Push Up",
        category="Strength",
        equipment_needed=False
    )
    squat = Exercise(
        name="Squat",
        category="Strength",
        equipment_needed=False
    )
    running = Exercise(
        name="Running",
        category="Cardio",
        equipment_needed=True
    )
    
    db.session.add_all([push_up, squat, running])
    db.session.commit()

    print("Seeding workouts...")
    workout_1 = Workout(
        date=date(2026x, 6, 1),
        duration_minutes=45,
        notes="Morning workout"
    )
    workout_2 = Workout(
        date=date(2026, 6, 3),
        duration_minutes=30,
        notes="Cardio session"
    )

    db.session.add_all([workout_1, workout_2])
    db.session.commit()

    print("Seeding workout exercises...")
    we_1 = WorkoutExercise(
        workout_id=workout_1.id,
        exercise_id=push_up.id,
        reps=15,
        sets=3,
        duration_seconds=60
    )
    we_2 = WorkoutExercise(
        workout_id=workout_1.id,
        exercise_id=squat.id,
        reps=20,
        sets=3,
        duration_seconds=90
    )
    we_3 = WorkoutExercise(
        workout_id=workout_2.id,
        exercise_id=running.id,
        reps=1,
        sets=1,
        duration_seconds=1800
    )

    db.session.add_all([we_1, we_2, we_3])
    db.session.commit()

    print("Database seeded successfully!")