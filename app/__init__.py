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

def find_event(event_id):
    """Helper to locate an event by its id."""
    return next((event for event in events if event.id == event_id), None)

# Root route provides API information for users who navigate to /
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Event Management API",
        "routes": {
            "create": "POST /events",
            "update": "PATCH /events/<id>",
            "delete": "DELETE /events/<id>"
        }
    }), 200

# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    request_data = request.get_json()

    if not request_data or "title" not in request_data:
        return jsonify({"error": "A title is required to create an event."}), 400

    new_id = max((event.id for event in events), default=0) + 1
    new_event = Event(new_id, request_data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


# List all events
@app.route("/events", methods=["GET"])
def list_events():
    """Return a JSON array of all events."""
    return jsonify([event.to_dict() for event in events]), 200

# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": "Event not found."}), 404

    request_data = request.get_json()
    if not request_data or "title" not in request_data:
        return jsonify({"error": "A title is required to update the event."}), 400

    event.title = request_data["title"]
    return jsonify(event.to_dict()), 200

# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": "Event not found."}), 404

    events.remove(event)
    return "", 204

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found."}), 404

# Error handler for 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed."}), 405

# Error handler for 500 Internal Server Error (for debugging)
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error."}), 500

__all__ = ["app", "Event", "events"]
