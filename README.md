# Event Management REST API

A RESTful API built with Flask that demonstrates full CRUD (Create, Read, Update, and Delete) operations for managing events. The application accepts JSON requests, returns JSON responses, and simulates data persistence using an in-memory list of `Event` objects.

## Features

* Create new events using a **POST** request.
* Update an existing event's title using a **PATCH** request.
* Delete an event using a **DELETE** request.
* Accept JSON request bodies with `request.get_json()`.
* Return structured JSON responses using `jsonify()`.
* Return appropriate HTTP status codes for successful and unsuccessful requests.

## Technologies Used

* Python 3
* Flask
* JSON
* Pytest

## Project Structure

```text
course-8-module-5-flask-full-crud-api-lab/
├── app.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── pytest.ini
```

## Installation

1. Clone the repository.

```bash
git clone git@github.com:wanja-juma/course-8-module-5-flask-full-crud-api-lab.git
```

2. Navigate to the project directory.

```bash
cd course-8-module-5-flask-full-crud-api-lab
```

3. Install the project dependencies.

```bash
pipenv install
```

4. Activate the virtual environment.

```bash
pipenv shell
```

## Running the Application

Start the Flask development server:

```bash
flask --app app run
```

or

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Create an Event

**Endpoint**

```http
POST /events
```

**Request Body**

```json
{
  "title": "Hackathon"
}
```

**Success Response**

**Status Code:** `201 Created`

```json
{
  "id": 3,
  "title": "Hackathon"
}
```

---

### Update an Event

**Endpoint**

```http
PATCH /events/<id>
```

**Request Body**

```json
{
  "title": "Hackathon 2025"
}
```

**Success Response**

**Status Code:** `200 OK`

```json
{
  "id": 1,
  "title": "Hackathon 2025"
}
```

**Error Response**

**Status Code:** `404 Not Found`

```json
{
  "error": "Event not found"
}
```

---

### Delete an Event

**Endpoint**

```http
DELETE /events/<id>
```

Deletes the specified event.

**Success Response**

**Status Code:** `204 No Content`

**Error Response**

**Status Code:** `404 Not Found`

```json
{
  "error": "Event not found"
}
```

## HTTP Status Codes

| Status Code         | Description                           |
| ------------------- | ------------------------------------- |
| **201 Created**     | A new event was created successfully. |
| **200 OK**          | An event was updated successfully.    |
| **204 No Content**  | An event was deleted successfully.    |
| **404 Not Found**   | The requested event does not exist.   |
| **400 Bad Request** | Invalid or missing request data.      |

## Testing the API

You can test the endpoints using an API client such as Postman or with `curl`.

### Create an Event

```bash
curl -X POST http://127.0.0.1:5000/events \
-H "Content-Type: application/json" \
-d '{"title":"Hackathon"}'
```

### Update an Event

```bash
curl -X PATCH http://127.0.0.1:5000/events/1 \
-H "Content-Type: application/json" \
-d '{"title":"Hackathon 2025"}'
```

### Delete an Event

```bash
curl -X DELETE http://127.0.0.1:5000/events/2
```

## Running the Tests

Run the automated test suite with:

```bash
pytest
```

A successful run should report all tests passing.

## Author

Ruth Juma
