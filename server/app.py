from flask import Flask, make_response
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here

@app.route('/workouts', methods=['GET'])
def list_all_workouts():
    pass

@app.route('/workouts/<id>', methods=['GET'])
def get_workout(id):
    pass

@app.route('/workouts', methods=['POST'])
def post_workout():
    pass

@app.route('/workouts/<id>', methods=['DELETE'])
def delete_workout():
    pass

@app.route('/exercises', methods=['GET'])
def list_all_exercises():
    pass

@app.route('/exercises/<id>', methods=['GET'])
def get_exercise(id):
    pass

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