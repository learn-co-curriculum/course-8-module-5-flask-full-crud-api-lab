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

# ------------------------
# CREATE (POST /events)
# ------------------------
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_id = max([event.id for event in events], default=0) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


# ------------------------
# UPDATE (PATCH /events/<id>)
# ------------------------
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    for event in events:
        if event.id == event_id:
            event.title = data["title"]
            return jsonify(event.to_dict()), 200

    return jsonify({"error": "Event not found"}), 404


# ------------------------
# DELETE (DELETE /events/<id>)
# ------------------------
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    for event in events:
        if event.id == event_id:
            events.remove(event)
            return "", 204   # ✅ IMPORTANT for tests

    return jsonify({"error": "Event not found"}), 404


# ------------------------
# RUN APP
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)