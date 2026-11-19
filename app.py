
from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {"id": 1, "name": "Computer Science", "duration": "4 years"},
    {"id": 2, "name": "Information Science", "duration": "4 years"},
    {"id": 3, "name": "Electronics", "duration": "4 years"},
    {"id": 4, "name": "Mechanical Engineering", "duration": "4 years"}
]

@app.route("/")
def home():
    return jsonify({"message": "University Course Listing API"})

@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify(courses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
