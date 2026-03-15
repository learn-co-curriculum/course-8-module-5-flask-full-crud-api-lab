# Events RESTful API

A lightweight Flask-based RESTful API for managing events with full CRUD operations.

## Overview

This API provides endpoints to create, read, update, and delete event resources. It uses an in-memory data store for demonstration purposes and returns structured JSON responses with appropriate HTTP status codes.

## Features

- **Create Events** - POST `/events`
- **Update Events** - PATCH `/events/<id>`
- **Delete Events** - DELETE `/events/<id>`
- **List Events** - GET `/events` (implicit)
- **Root Endpoint** - GET `/` with routing information

## Requirements

- Python 3.7+
- Flask

## Installation

```bash
# Install dependencies
pip install flask

# Or use Pipfile
pipenv install
```

## Running the Server

```bash
python app.py
```

The server will start on `http://127.0.0.1:5000/`

## API Endpoints

### Root Endpoint

```
GET /
```

Returns API status and available routes.

### Create Event

```
POST /events
Content-Type: application/json

{
  "title": "Event Title"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "title": "Event Title"
}
```

### Update Event

```
PATCH /events/<id>
Content-Type: application/json

{
  "title": "Updated Title"
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "title": "Updated Title"
}
```

### Delete Event

```
DELETE /events/<id>
```

**Response:** `204 No Content`

## Error Handling

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - Missing required field |
| 404 | Not Found - Event ID does not exist |
| 405 | Method Not Allowed |

Example error response:
```json
{
  "error": "Event not found"
}
```

## Testing

Run tests with pytest:

```bash
pytest
```

## Project Structure

```
.
├── app.py          # Main application file
├── README.md       # This file
├── Pipfile         # Dependency definitions
├── pytest.ini      # Pytest configuration
└── tests/
    ├── __init__.py
    └── test_app.py # Unit tests
```

## License

MIT
