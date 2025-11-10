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

@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing 'title' field"}), 400
    new_event = Event(id=len(events) + 1, title=data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json()
    event = next((e for e in events if e.id == event_id), None)
    if not event:
        return ("Event not found", 404)
    if "title" in data:
        event.title = data["title"]
    return jsonify(event.to_dict())


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events
    event = next((e for e in events if e.id == event_id), None)
    if not event:
        return ({"error": "Event not found"}, 404)
    events = [e for e in events if e.id != event_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
