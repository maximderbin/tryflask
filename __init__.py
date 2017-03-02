from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/users/<int:id>")
def show(id):
  return jsonify(
    id=id,
    name="Foo Bar"
  )

if __name__ == "__main__":
  app.run()
