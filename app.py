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


# Root route so hitting http://127.0.0.1:5000/ works in the browser
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Events API is running",
        "routes": {
            "create_event": "POST /events",
            "update_event": "PATCH /events/<id>",
            "delete_event": "DELETE /events/<id>"
        }
    }), 200


# Helper function to find an event by id
def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None


# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # Validate input
    if not data or "title" not in data:
        return jsonify({"error": "Missing 'title' in request body"}), 400

    # Generate a new id based on current events
    new_id = max((event.id for event in events), default=0) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing 'title' in request body"}), 400

    event.title = data["title"]

    return jsonify(event.to_dict()), 200


# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    events.remove(event)

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
