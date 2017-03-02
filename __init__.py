from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/users")
def index():
  return jsonify([
    { "id": 1, "name": "Foo Bar" },
    { "id": 2, "name": "Foo Bar" },
    { "id": 3, "name": "Foo Bar" },
    { "id": 4, "name": "Foo Bar" },
    { "id": 5, "name": "Foo Bar" }
  ])

@app.route("/users/<int:id>")
def show(id):
  return jsonify(
    id=id,
    name="Foo Bar"
  )

if __name__ == "__main__":
  app.run()
