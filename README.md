# WORKOUT TRACKER
A lightweight Flask REST API (app.py) using Flask-SQLAlchemy, Marshmallow and Flask-Migrate for managing workouts, exercises and fitness routines.

## HOW TO RUN
1. Run `pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flask-migrate` (or `pipenv install` then `pipenv shell`)
2. Run `flask db upgrade` to create the databse tables, then run `python seed.py` to populate initial data
3. Run `python app.py`

## API ENDPOINTS
- `GET /workouts` - Lists all workouts
- `GET /workouts/<id>` - Gets a specific workout
- `POST /workouts` - Creates a workout
- `DELETE /workouts/<id>` - Deletes a workout
- `GET /exercises` - Lists all exercises
- `GET /exercises/<id>` - Gets a specific exercise
- `POST /exercises` - Creates an exercise
- `DELETE /exercises/<id>` - Deletes an exercise
- `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` - Adds an exercise to a workout

### SAMPLE JSON DATA FOR API TESTING

- Creating a new exercise (`POST /exercises`): 
{
  "name": "Pull-up",
  "category": "Strength",
  "equipment_needed": true
}

- Creating a new workout (`POST /workouts`): 
{
  "date": "2026-06-05",
  "duration_minutes": 50,
  "notes": "Leg day session"
}

- Adding an exercise to a workout(`POST /workouts/1/exercises/1/workout_exercises`): 
{
  "reps": 12,
  "sets": 3,
  "duration_seconds": 45
}

