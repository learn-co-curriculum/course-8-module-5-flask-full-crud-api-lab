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

# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing required field: title"}), 400
    
        #Implement the Loop and Process Each Element
    new_id = max((e.id for e in events), default=0) +1
    new_event = Event(new_id, data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201 # Return and Handle Results

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        return jsonify({"error": f"Event {event_id} not found"}), 404
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing required field: title"}), 400
    event.title = data["title"] #Implement the Loop and Process Each Element
    return jsonify(event.to_dict()), 200 # Return and Handle Results

# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        return jsonify({"error": f"Event {event_id} not found"}), 404

    events.remove(event) # Implement the Loop and Process Each Element
    return jsonify({"message": f"Event {event_id} deleted"}), 200 # Return and Handle Results

if __name__ == "__main__":
    app.run(debug=True)
