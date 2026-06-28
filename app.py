from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


# Helper function to avoid repeating the "find by id" lookup logic
def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None


# Welcome route - confirms the API is running
@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Event Management API"})


# GET /events - Return all events as a JSON array
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200


# Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # Task 2 - Design and Develop the Code
    data = request.get_json()

    # Input validation: make sure title was provided
    if not data or "title" not in data:
        return jsonify({"error": "Missing required field: title"}), 400

    # Task 3 - Implement the Loop and Process Each Element
    # Generate a new id by taking the max existing id + 1 (handles empty list too)
    new_id = max((event.id for event in events), default=0) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    # Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()), 201


# Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # Task 2 - Design and Develop the Code
    event = find_event(event_id)

    # Task 4 - Return and Handle Results (not found case)
    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404

    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing required field: title"}), 400

    # Task 3 - Implement the Loop and Process Each Element (mutate matched record)
    event.title = data["title"]

    # Task 4 - Return and Handle Results
    return jsonify(event.to_dict()), 200


# Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # Task 2 - Design and Develop the Code
    event = find_event(event_id)

    # Task 4 - Return and Handle Results (not found case)
    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404

    # Task 3 - Implement the Loop and Process Each Element (remove matched record)
    events.remove(event)

    # Task 4 - Return and Handle Results
    # 204 No Content means success with no body
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)