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

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input


@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()
    # TODO: Task 3 - Implement the Loop and Process Each Element
    
    new_id = max((e.id for e in events)) + 1 if events else 1
    new_event = Event(new_id, data['title'])
    events.append(new_event)
    
    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()
    event = next((e for e in events if e.id == event_id), None)
    # TODO: Task 3 - Implement the Loop and Process Each Element
    if not event:
        return jsonify({"error": "Not Found", "message": "Event ID not found"}), 404
    
    if "title" in data:
        event.title = data["title"]
        
    return jsonify(event.to_dict()), 200

    # TODO: Task 4 - Return and Handle Results


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 1 - Define the Problem
    # Remove an event from the list
    # TODO: Task 2 - Design and Develop the Code
    global events
    # TODO: Task 3 - Implement the Loop and Process Each Element
    event_to_remove = next((e for e in events if e.id == event_id), None)
    if event_to_remove:
        events = [e for e in events if e.id != event_id]
        return jsonify({"message": f"Event {event_id} deleted successfully"}), 204
    
    # TODO: Task 4 - Return and Handle Results
    return jsonify({"error": "Not Found", "message": "Event ID not found"}), 404


@app.route("/events", methods=["GET"])
def get_all_events():
    return jsonify([e.to_dict() for e in events])


if __name__ == "__main__":
    app.run(debug=True)
