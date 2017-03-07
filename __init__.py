from flask import Flask
from flask import jsonify
from db import users
app = Flask(__name__)

@app.route('/users')
def index():
  return jsonify(users())

@app.route('/users/<int:id>')
def show(id):
  return jsonify(next((x for x in users() if x['id'] == id), None))

if __name__ == '__main__':
  app.run()
