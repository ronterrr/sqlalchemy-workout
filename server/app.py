from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()

# Define Routes here

@app.route('/workouts', methods=['GET'])
def list_all_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200


@app.route('/workouts/<id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({"Error": "Workout not found"}), 404
    return jsonify(workout_schema.dump(workout)), 200


@app.route('/workouts', methods=['POST'])
def post_workout():
    data = request.get_json()
    try:
        new_workout = workout_schema.load(data, session=db.session)
        db.session.add(new_workout)
        db.session.commit()
        return jsonify(workout_schema.dump(new_workout)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'Error': str(e)}), 400


@app.route('/workouts/<id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({'Error': 'workout not found'}), 404

    db.session.delete(workout)
    db.session.commit()
    return jsonify({'message': 'workout deleted successfully'}), 200


@app.route('/exercises', methods=['GET'])
def list_all_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200


@app.route('/exercises/<id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({'error': 'Exercise not found'}), 404
    return jsonify(exercise_schema.dump(exercise)), 200


@app.route('/exercises', methods=['POST'])
def post_exercise():
    data = request.get_json()
    try:
        new_exercise = exercise_schema.load(data, session=db.session)
        db.session.add(new_exercise)
        db.session.commit()
        return jsonify(exercise_schema.dump(new_exercise)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'Error': str(e)}), 400


@app.route('/exercises/<id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({'error': 'exercise not found'}), 404

    db.session.delete(exercise)
    db.session.commit()
    return jsonify({'message': 'deletion successful'}), 200


@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)

    if not workout or not exercise:
        return jsonify({"Error": "Workout Or Exercise not found"}), 401

    data = request.get_json()
    data['workout_id'] = workout_id
    data['exercise_id'] = exercise_id

    try:
        workout_exercise = workout_exercise_schema.load(data, session=db.session)
        db.session.add(workout_exercise)
        db.session.commit()
        return jsonify(workout_exercise_schema.dump(workout_exercise)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'Error': str(e)}), 400



if __name__ == '__main__':
    app.run(port=5555, debug=True)