from flask import Flask

app = Flask(__name__)


# creatingt the Home Page
@app.route("/")
def hello_world():
  return "<p>Hello, Drivah!!!</p>"


if (__name__) == "__main__":
  app.run(host='0.0.0.0', debug=True)
