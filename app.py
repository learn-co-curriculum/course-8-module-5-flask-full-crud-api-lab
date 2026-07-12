

    from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data model
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory database simulation
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# --- API ROUTES ---

# POST /events - Create a new event from JSON input
@app.route('/events', methods=['POST'])
def create_event():
    # Parse JSON data from the request body
    data = request.get_json()
    
    # Validate that title is provided
    if not data or 'title' not in data:
        return jsonify({"error": "Bad Request", "message": "Title is required"}), 400
    
    # Generate a new unique ID based on the current maximum ID in the list
    new_id = max([event.id for event in events], default=0) + 1
    
    # Create the new Event instance and append it to our in-memory list
    new_event = Event(id=new_id, title=data['title'])
    events.append(new_event)
    
    # Return the newly created event and a 201 Created status code
    return jsonify(new_event.to_dict()), 201


# PATCH /events/<id> - Update the title of an event
@app.route('/events/<int:id>', methods=['PATCH'])
def update_event(id):
    # Parse JSON data from the request body
    data = request.get_json()
    
    # Validate that title is provided in the update payload
    if not data or 'title' not in data:
        return jsonify({"error": "Bad Request", "message": "Title is required to update"}), 400

    # Search for the event matching the provided ID
    for event in events:
        if event.id == id:
            # Update the event's title
            event.title = data['title']
            # Return the updated event object with a 200 OK status code
            return jsonify(event.to_dict()), 200
            
    # If no event matches the ID, return a 404 Not Found error
    return jsonify({"error": "Not Found", "message": f"Event with ID {id} does not exist"}), 404


# DELETE /events/<id> - Remove an event from the list
@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    # Search for the event matching the provided ID
    for event in events:
        if event.id == id:
            # Remove the event from our in-memory list
            events.remove(event)
            # Return a success message with a 200 OK status code
            return jsonify({"message": f"Event with ID {id} has been deleted successfully"}), 200
            
    # If no event matches the ID, return a 404 Not Found error
    return jsonify({"error": "Not Found", "message": f"Event with ID {id} does not exist"}), 404


if __name__ == "__main__":
    app.run(debug=True)
