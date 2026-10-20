from flask import Flask, make_response
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()

# Define Routes here

@app.route('/workouts', methods=['GET'])
def list_all_workouts():
    workouts = Workout.query.all()
    return make_response(workouts_schema.jsonify(workouts), 200)


@app.route('/workouts/<id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return make_response({"Error": "Workout not found"}, 404)
    return make_response(workout_schema.jsonify(workout), 200)


@app.route('/workouts', methods=['POST'])
def post_workout():
    pass

@app.route('/workouts/<id>', methods=['DELETE'])
def delete_workout():
    pass


@app.route('/exercises', methods=['GET'])
def list_all_exercises():
    exercises = Exercise.query.all()
    return make_response(exercise_schema.jsonify(exercises), 200)


@app.route('/exercises/<id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return make_response({'error': 'Exercise not found'}, 404)
    return make_response(exercise_schema.jsonify(exercise), 200)


@app.route('/exercises', methods=['POST'])
def post_exercise():
    pass

@app.route('/exercises/<id>', methods=['DELETE'])
def delete_exercise(id):
    pass

@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises')
def add_exercise_to_workout(workout_id, exercise_id):
    pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)