# Event Management API

## Overview

This project is a simple RESTful API built with **Python** and **Flask**. It demonstrates how to perform CRUD operations using in-memory data storage without a database.

The API allows users to:

- Create a new event
- Update an existing event
- Delete an event

Data is stored in a Python list of `Event` objects while the application is running.

---

## Features

- Create events using **POST**
- Update event titles using **PATCH**
- Delete events using **DELETE**
- Accept JSON input with `request.get_json()`
- Return JSON responses using `jsonify()`
- Handle invalid requests with appropriate HTTP status codes

---

## Technologies Used

- Python 3
- Flask

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd <project-folder>
```

Install dependencies:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

# API Routes

## Create Event

**POST** `/events`

### Request

```json
{
    "title": "Hackathon"
}
```

### Success Response

**Status Code:** `201 Created`

```json
{
    "id": 3,
    "title": "Hackathon"
}
```

---

## Update Event

**PATCH** `/events/<event_id>`

Example:

```
PATCH /events/1
```

### Request

```json
{
    "title": "Hackathon 2025"
}
```

### Success Response

**Status Code:** `200 OK`

```json
{
    "id": 1,
    "title": "Hackathon 2025"
}
```

---

## Delete Event

**DELETE** `/events/<event_id>`

Example:

```
DELETE /events/2
```

### Success Response

**Status Code:** `204 No Content`

No response body is returned.

---

# Error Responses

## Missing Title

**Status Code:** `400 Bad Request`

```json
{
    "error": "Title is required"
}
```

---

## Event Not Found

**Status Code:** `404 Not Found`

```json
{
    "error": "Event not found"
}
```

---

# Testing

The API was tested using **Postman**.

The following endpoints were successfully tested:

- POST `/events`
- PATCH `/events/<event_id>`
- DELETE `/events/<event_id>`

---

# Project Structure

```
.
├── app.py
└── README.md
```

---

# Future Improvements

- Add GET endpoints to retrieve events
- Store data using a database such as SQLite
- Validate input more thoroughly
- Separate routes, models, and configuration into different modules

---

## Author

**Debbie Obiki**