# Hotel Booking API

A simple and efficient Hotel Booking Management System built with FastAPI. This API provides endpoints to manage hotel room bookings with full CRUD (Create, Read, Update, Delete) operations.

## Features

- ✨ Create new room bookings
- 📋 View all bookings
- 🔍 Get specific booking details by ID
- ✏️ Update existing bookings
- 🗑️ Delete bookings
- ✅ Duplicate room number validation
- ⚡ Fast and lightweight using FastAPI
- 📝 Automatic API documentation with Swagger UI

## Technology Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Python 3.7+** - Programming language

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Simbu06/fastapi.git
cd fastapi
```

2. Create a virtual environment:
```bash
python -m venv fastapi-env
```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     fastapi-env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source fastapi-env/bin/activate
     ```

4. Install required dependencies:
```bash
pip install fastapi uvicorn pydantic
```

## Running the Application

Start the server using uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Documentation

Once the server is running, you can access:
- **Interactive API documentation (Swagger UI)**: http://127.0.0.1:8000/docs
- **Alternative API documentation (ReDoc)**: http://127.0.0.1:8000/redoc

## API Endpoints

### Root Endpoint
- **GET** `/`
  - Returns a welcome message
  - Response: `{"msg": "Welcome to the Hotel Booking API"}`

### Get All Bookings
- **GET** `/bookings`
  - Returns a list of all room bookings
  - Response: Array of booking objects

### Get Booking by ID
- **GET** `/booking/{id}`
  - Returns details of a specific booking
  - Parameters: `id` (integer) - Booking ID
  - Response: Booking object
  - Error: 404 if booking not found

### Create New Booking
- **POST** `/booking/`
  - Creates a new room booking
  - Request Body:
    ```json
    {
      "id": 3,
      "user_name": "Alice",
      "room_no": 103
    }
    ```
  - Response: Created booking object
  - Errors:
    - 400 if room number already booked
    - 400 if booking ID already exists

### Update Booking
- **PUT** `/booking/{id}`
  - Updates an existing booking
  - Parameters: `id` (integer) - Booking ID
  - Request Body (partial update):
    ```json
    {
      "user_name": "Updated Name",
      "room_no": 105
    }
    ```
  - Response: `{"msg": "Booking updated successfully"}`
  - Error: 404 if booking not found

### Delete Booking
- **DELETE** `/booking/{id}`
  - Deletes a booking
  - Parameters: `id` (integer) - Booking ID
  - Response: `{"msg": "Booking deleted successfully"}`
  - Error: 404 if booking not found

## Data Models

### Rooms
```python
{
  "id": int,
  "user_name": str,
  "room_no": int
}
```

### Update_room
```python
{
  "user_name": Optional[str],
  "room_no": Optional[int]
}
```

## Usage Examples

### Using cURL

**Get all bookings:**
```bash
curl http://127.0.0.1:8000/bookings
```

**Create a new booking:**
```bash
curl -X POST "http://127.0.0.1:8000/booking/" \
     -H "Content-Type: application/json" \
     -d '{"id": 3, "user_name": "Alice", "room_no": 103}'
```

**Update a booking:**
```bash
curl -X PUT "http://127.0.0.1:8000/booking/1" \
     -H "Content-Type: application/json" \
     -d '{"user_name": "Updated Name"}'
```

**Delete a booking:**
```bash
curl -X DELETE "http://127.0.0.1:8000/booking/1"
```

### Using Python Requests

```python
import requests

# Get all bookings
response = requests.get("http://127.0.0.1:8000/bookings")
print(response.json())

# Create a new booking
new_booking = {
    "id": 3,
    "user_name": "Alice",
    "room_no": 103
}
response = requests.post("http://127.0.0.1:8000/booking/", json=new_booking)
print(response.json())
```

## Project Structure

```
fastapi/
├── main.py          # Main application file with API endpoints
├── models.py        # Pydantic models for data validation
├── fastapi-env/     # Virtual environment directory
└── README.md        # Project documentation
```

## Future Enhancements

- 🗄️ Add database integration (PostgreSQL/MongoDB)
- 🔐 Implement authentication and authorization
- 📅 Add date-based booking system
- 💳 Payment integration
- 📧 Email notifications
- 🔍 Advanced search and filtering
- 📊 Analytics and reporting

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Simbu06**
- GitHub: [@Simbu06](https://github.com/Simbu06)

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Inspired by modern REST API design principles
