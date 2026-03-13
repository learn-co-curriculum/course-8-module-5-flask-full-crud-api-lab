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
    request_data = request.get_json()   # Data from POST request

    new_id = max([e.id for e in events]) + 1 if events else 1
    request_body = Event(id=new_id, title=request_data['title'])

    # Adding data to the In-memory 'database'
    events.append(request_body)

    #Returning the response
    return jsonify(request_body.to_dict()), 201

@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    request_data = request.get_json()

    #Finding the event in the array events
    event =  next((e for e in events if e.id == event_id), None)
    if event == None:
        return('Event not found', 404)
    
    if 'title' in request_data:
        event.title = request_data['title']
    return jsonify(event.to_dict()), 200


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events

    #Searching for event
    event = next((e for e in events if e.id == event_id), None)
    if event == None:
        return('Event not found', 404)
    

    events = next(e for e in events if e.id != event_id)
    return('Event removed', 204)
    

if __name__ == "__main__":
    app.run(debug=True)
