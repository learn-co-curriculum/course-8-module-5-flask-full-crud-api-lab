from flask import Flask, jsonify, request

app = Flask(__name__)


class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


events = [Event(1, "Tech Meetup"), Event(2, "Python Workshop")]


@app.route("/events", methods=["POST"])
def create_event():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"ERROR": "No JSON body provided"}), 400

        title = data.get("title")
        if not title:
            return jsonify({"ERROR": "Missing title"}), 400

        new_id = max(e.id for e in events) + 1
        event = Event(id=new_id, title=title)
        events.append(event)

        return jsonify(event.to_dict()), 201

    except Exception as e:
        print(str(e))
        return jsonify({"ERROR": "Internal server error"}), 500


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    try:
        data = request.get_json()
        event = next((e for e in events if e.id == event_id), None)

        if not event:
            return jsonify({"ERROR": "Event not found"}), 404

        title = data.get("title")
        if not title:
            return jsonify({"ERROR": "Missing title"}), 400

        event.title = title

        return jsonify(event.to_dict()), 200

    except Exception as e:
        print(str(e))
        return jsonify({"ERROR": "Internal server error"}), 500


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    try:

        event = next((e for e in events if e.id == event_id), None)

        if not event:
            return jsonify({"ERROR": "Event not found"}), 404

        events.remove(event)

        return "", 204

    except Exception as e:
        print(str(e))
        return jsonify({"ERROR": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
