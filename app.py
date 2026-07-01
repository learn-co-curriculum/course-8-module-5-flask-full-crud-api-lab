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

    data = request.get_json() #reads the incoming JSON
    event_id = max((event.id for event in events), default=0) + 1 #auto-generate ID
    title = data.get("title")

    #creating event object and appending it to the list
    new_event = Event(id=event_id, title=title)
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = next((e for e in events if e.id == id), None)

    if event is None:
        return jsonify ({"error": "Event not found"}), 404
    
    data = request.get_json()
    #log.info("update_event_request", id=id, request_data=data)

    if "eventTitle" in data:
        event.title = data["eventTitle"]
    
    return jsonify (event.to_dict()), 200
    

# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events

    event = next((e for e in events if e.id ==id), None)

    if event is None:
        return jsonify({"error": "Event not found"}), 404

    events = [e for e in events if e.id != id]

    return jsonify ({"message": f"Event {id} deleted"}), 200

# View for getting details of an event that matches ID in URL - GET
@app.route("/customers/<int:id>", methods=["GET"])
def get_event(id):
    event = next((e for e in events if e.id == id), None) #looping to find customer with the id

    if event is None:
        return jsonify({"error": "Event not found. Please try again"}), 404 #confirm on error message display

    return jsonify(event.to_dict()), 200

if __name__ == "__main__":
    app.run(debug=True)
