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
    # Get the JSON body from the request
    data = request.get_json()
# check if there is data and if it has a "title"
    if not data or "title" not in data:
        # if not, return an error and status code 400
        return jsonify({"error": "Request JSON must include a 'title' field"}), 400
# Implement the Loop and Process Each Element 
    new_id = 1  # default id if there are no events
    for event in events:
        # keep track of the highest id and add 1
        if event.id >= new_id:
            new_id = event.id + 1

    # create a new Event object with the new id and the title from the JSON
    new_event = Event(new_id, data["title"])

    # add the new event to the in-memory "database"
    events.append(new_event)

    # Return and Handle Results
    return jsonify(new_event.to_dict()), 201

# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
  # get the JSON body from the request
    data = request.get_json()

 # check that there is a "title" in the JSON
    if not data or "title" not in data:
        return jsonify({"error": "Request JSON must include a 'title' field"}), 400
    
    # Task 3 - Implement the Loop and Process Each Element
    #try to find the event with the given id using a loop
    event_to_update = None
    for event in events:
        if event.id == event_id:
            event_to_update = event
            break

    # if we did not find an event, return 404
    if event_to_update is None:
        return jsonify({"error": "Event not found"}), 404

    # update the title of the event
    event_to_update.title = data["title"]

    # TODO: Task 4 - Return and Handle Results
    return jsonify(event_to_update.to_dict()), 200

# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # we will search for the event to delete
    event_to_delete = None

    # Implement the Loop and Process Each Element
    for event in events:
        if event.id == event_id:
            event_to_delete = event
            break
# if no event was found, return 404
    if event_to_delete is None:
        return jsonify({"error": "Event not found"}), 404

    # remove the event from the list
    events.remove(event_to_delete)
    
    # Return and Handle Results
    return "", 204

if __name__ == "__main__":
    app.run(debug=True, port=5001)
