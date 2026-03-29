# Flask Event Management API

## Overview

This is a simple **Event Management API** built using **Flask**.  
It allows users to:

- Create new events  
- Update existing event titles  
- Delete events  
- List all events  

The API uses an **in-memory list** of events to simulate database persistence. Responses are returned in **JSON format** with proper HTTP status codes.

---

## Routes

| Route | Method | Description | Example Request | Example Response |
|-------|--------|-------------|----------------|----------------|
| `/events` | GET | List all events | `curl http://127.0.0.1:5000/events` | `[{"id":1,"title":"Tech Meetup"},{"id":2,"title":"Python Workshop"}]` |
| `/events` | POST | Create a new event | `curl -X POST http://127.0.0.1:5000/events -H "Content-Type: application/json" -d '{"title":"Hackathon"}'` | `{"id":3,"title":"Hackathon"}` |
| `/events/<id>` | PATCH | Update an event title | `curl -X PATCH http://127.0.0.1:5000/events/1 -H "Content-Type: application/json" -d '{"title":"Hackathon 2025"}'` | `{"id":1,"title":"Hackathon 2025"}` |
| `/events/<id>` | DELETE | Remove an event | `curl -X DELETE http://127.0.0.1:5000/events/2` | No content (HTTP 204) |

---

## HTTP Status Codes

| Status Code | Meaning |
|------------|---------|
| 200 OK | PATCH request successful |
| 201 Created | POST request successful, event created |
| 204 No Content | DELETE request successful, event removed |
| 400 Bad Request | POST or PATCH missing required fields |
| 404 Not Found | Event with specified ID does not exist |

---

## Example Workflow

1. **Create a new event**
```bash
curl -X POST http://127.0.0.1:5000/events \
-H "Content-Type: application/json" \
-d '{"title": "Hackathon"}'

RESPONSE 
{
  "id": 3,
  "title": "Hackathon"
}

UPDATE AN EVENT TITLE

curl -X PATCH http://127.0.0.1:5000/events/1 \
-H "Content-Type: application/json" \
-d '{"title": "Hackathon 2025"}'

RESPONSE
{
  "id": 1,
  "title": "Hackathon 2025"
}

DELETE AN EVENT

curl -X DELETE http://127.0.0.1:5000/events/2

RESPONSE
No content (HTTP 204)

LIST ALL EVENTS

curl http://127.0.0.1:5000/events

RESPONSE
[
  {
    "id": 1,
    "title": "Hackathon 2025"
  },
  {
    "id": 3,
    "title": "Hackathon"
  }
]

