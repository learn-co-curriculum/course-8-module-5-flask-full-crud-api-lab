from flask import Flask, jsonify, request

app = Flask(__name__)

# Root route
@app.route("/", methods=["GET"])
def root():
    return jsonify({
        "message": "Event Management API",
        "endpoints": {
            "GET /": "API information",
            "GET /events": "List all events",
            "GET /events/<id>": "Get single event",
            "POST /events": "Create new event",
            "PATCH /events/<id>": "Update event title",
            "DELETE /events/<id>": "Delete event"
        }
    }), 200

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


def get_event_by_id(event_id):
    """Helper: return Event instance by id or None."""
    for e in events:
        if e.id == event_id:
            return e
    return None

# Get all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([e.to_dict() for e in events]), 200

# Get single event
@app.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    evt = get_event_by_id(event_id)
    if not evt:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(evt.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    title = data.get("title")
    if not title or not isinstance(title, str):
        return jsonify({"error": "'title' is required"}), 400

    # Determine next id
    next_id = max((e.id for e in events), default=0) + 1
    new_event = Event(next_id, title)
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    evt = get_event_by_id(event_id)
    if not evt:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    title = data.get("title")
    if not title or not isinstance(title, str):
        return jsonify({"error": "'title' is required"}), 400

    evt.title = title
    return jsonify(evt.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    evt = get_event_by_id(event_id)
    if not evt:
        return jsonify({"error": "Event not found"}), 404

    # remove event
    events.remove(evt)
    # 204 No Content
    return ("", 204)

if __name__ == "__main__":
    app.run(debug=True)
