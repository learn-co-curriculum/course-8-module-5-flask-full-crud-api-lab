from flask import Flask, jsonify, request

# Create the Flask application instance
app = Flask(__name__)

# Simulated data model
class Event:
    """
    Represents an event with an ID and title.
    """

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        """
        Convert the Event object into a dictionary.
        """
        return {
            "id": self.id,
            "title": self.title
        }
# In-memory list acting as a database
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# POST /events
# Create a new event from JSON input.

@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # Validate request body
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Generate the next available ID
    new_id = max(event.id for event in events) + 1 if events else 1

    # Create and store the new event
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201

# PATCH /events/<id>
# Update an existing event title.

@app.route("/events/<int:id>", methods=["PATCH"])
def update_event(id):
    data = request.get_json()

    # Find the event
    event = next((event for event in events if event.id == id), None)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    # Update title if provided
    if "title" in data:
        event.title = data["title"]

    return jsonify(event.to_dict()), 200

# DELETE /events/<id>
# Remove an event from the list.

@app.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):
    # Find the event by ID
    event = next((event for event in events if event.id == id), None)

    # Return 404 if the event doesn't exist
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    # Remove the event from the list
    events.remove(event)

    # Return 204 No Content on successful deletion
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
