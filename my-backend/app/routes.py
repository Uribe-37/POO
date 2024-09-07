from flask import request, jsonify
from app import app, db
from app.models import User

@app.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  new_user = User(username=data['username'], password=data['password'])
  db.session.add(new_user)
  db.session.commit()
  return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  user = User.query.filter_by(username=data['username']).first()
  if user and user.password == data['password']:
    return jsonify({'message': 'Login successful'})
  return jsonify({'message': 'Invalid credentials'})
