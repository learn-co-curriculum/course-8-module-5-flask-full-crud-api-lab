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

# --- Mandatory Extra Routes For Grading ---

# 1. Root Route Welcome Message
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Event Management API!"}), 200

# 2. GET /events - Retrieve all events
@app.route("/events", methods=["GET"])
def get_events():
    # Convert list of Event objects into a list of dictionaries
    return jsonify([event.to_dict() for event in events]), 200


# --- Lab CRUD Assignments ---

# 3. POST /events - Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # Read the JSON payload data sent by client
    data = request.get_json()
    
    # Validation check: Ensure they provided a title
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
        
    # Generate an incremental ID safely
    new_id = events[-1].id + 1 if events else 1
    
    # Create new instance and append to list
    new_event = Event(id=new_id, title=data["title"])
    events.append(new_event)
    
    # Return the new resource with a 201 Created status
    return jsonify(new_event.to_dict()), 201


# 4. PATCH /events/<int:event_id> - Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json()
    
    # Loop and search for matching element
    for event in events:
        if event.id == event_id:
            if data and "title" in data:
                event.title = data["title"]
            return jsonify(event.to_dict()), 200
            
    # Return result if loop finishes without finding the ID
    return jsonify({"error": "Event not found"}), 404


# 5. DELETE /events/<int:event_id> - Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events
    
    # Loop and search for matching element
    for event in events:
        if event.id == event_id:
            events.remove(event)
            # 204 Content Success means empty body response string
            return "", 204
            
    # Return error result if target element doesn't exist
    return jsonify({"error": "Event not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
