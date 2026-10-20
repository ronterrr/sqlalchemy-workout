from flask import Flask, make_response, request
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
    data = request.get_json()
    try:
        new_workout = workout_schema.load(data, session=db.session)
        db.session.add(new_workout)
        db.session.commit()
        return make_response(workout_schema.jsonify(new_workout), 201)
    except Exception as e:
        db.session.rollback()
        return make_response({'Error': str(e)}, 400)

@app.route('/workouts/<id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return make_response({'Error': 'workout not found'}, 404)

    db.session.delete(workout)
    db.session.commit()
    return make_response({'message': 'workout deleted successfully'}, 200)


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
    data = request.get_json()
    try:
        new_exercise = exercise_schema.load(data, session=db.session)
        db.session.add(new_exercise)
        db.session.commit()
        return make_response({exercise_schema.jsonify(new_exercise), 200})
    except Exception as e:
        db.session.rollback()
        return make_response({'Error': str(e)}, 400)

@app.route('/exercises/<id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return make_response({'error': 'exercise not found'}, 404)

    db.session.delete(exercise)
    db.session.commit()
    return make_response({'message': 'deletion successful'}, 200)

@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises')
def add_exercise_to_workout(workout_id, exercise_id):
    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)

    if not workout or not exercise:
        return make_response({"Error": "Workout Or Exercise not found"}, 401)

    data = request.get_json()
    data['workout_id'] = workout_id
    data['exercise_id'] = exercise_id

    try:
        workout_exercise = workout_exercise_schema.load(data, session=db.session)
        db.session.add(workout_exercise)
        db.session.commit()
        return make_response(workout_exercise_schema.jsonify(workout_exercise), 200)
    except Exception as e:
        db.rollback()
        return make_response({'Error': str(e)}, 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)