# Event Management API

A simple RESTful API built with Flask that supports full CRUD operations on event data. Events are stored in memory (no database), making this a lightweight demonstration of route design, JSON handling, and HTTP status code conventions.

## Features

- List all events
- Create a new event
- Update an existing event's title
- Delete an event
- Structured JSON responses with appropriate HTTP status codes
- Input validation with clear error messages

## Tech Stack

- Python 3
- Flask

## Setup

1. Clone the repository and navigate into it.
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the server:
   ```bash
   python app.py
   ```
4. The API will be available at `http://localhost:5000`.

## Routes

### `GET /`

Welcome message confirming the API is running.

**Response — `200 OK`**
```json
{
  "message": "Welcome to the Event Management API"
}
```

---

### `GET /events`

Returns a list of all events.

**Response — `200 OK`**
```json
[
  { "id": 1, "title": "Tech Meetup" },
  { "id": 2, "title": "Python Workshop" }
]
```

---

### `POST /events`

Creates a new event. Requires a `title` field in the JSON body.

**Request**
```json
{ "title": "Hackathon" }
```

**Response — `201 Created`**
```json
{ "id": 3, "title": "Hackathon" }
```

**Error response — `400 Bad Request`** (missing `title`)
```json
{ "error": "Missing required field: title" }
```

---

### `PATCH /events/<id>`

Updates the title of an existing event. Requires a `title` field in the JSON body.

**Request**
```
PATCH /events/1
```
```json
{ "title": "Hackathon 2025" }
```

**Response — `200 OK`**
```json
{ "id": 1, "title": "Hackathon 2025" }
```

**Error response — `404 Not Found`** (no event with that id)
```json
{ "error": "Event with id 99 not found" }
```

**Error response — `400 Bad Request`** (missing `title`)
```json
{ "error": "Missing required field: title" }
```

---

### `DELETE /events/<id>`

Removes an event by id.

**Request**
```
DELETE /events/2
```

**Response — `204 No Content`**

No response body.

**Error response — `404 Not Found`** (no event with that id)
```json
{ "error": "Event with id 99 not found" }
```

## Testing

Automated tests are included in `test_app.py`. Run them with:

```bash
pip install pytest
python -m pytest test_app.py -v
```

You can also test manually with `curl`, Postman, or a browser (for `GET` routes). Example with curl:

```bash
curl -X POST http://localhost:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title": "Hackathon"}'
```

## Design Notes

- **In-memory storage**: Events are stored in a Python list and reset every time the server restarts. This simulates a database for learning purposes but isn't persistent.
- **Helper function for lookups**: A `find_event(event_id)` helper avoids repeating the same search logic across the `PATCH` and `DELETE` routes.
- **Validation order**: For `PATCH`, the existence check (404) runs before the input validation check (400), so a request to a nonexistent event correctly reports "not found" rather than a misleading "missing field" error.
- **Future improvements**: Replace the in-memory list with a real database (e.g. SQLite via SQLAlchemy) to persist data across restarts, and split routes into blueprints as the API grows.