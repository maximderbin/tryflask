from flask import jsonify
from tryflask import app
from tryflask.db import users

@app.route('/users')
def index():
  return jsonify(users())

@app.route('/users/<int:id>')
def show(id):
  return jsonify(next((x for x in users() if x['id'] == id), None))
