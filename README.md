# 🚚 Freight Load Management REST API

A RESTful backend service for managing freight shipment loads, including origin and destination tracking, truck allocation, shipment details, and shipper management.

Built using **Flask**, **SQLAlchemy**, and **Marshmallow**, this project demonstrates REST API design, database modeling, data validation, and CRUD operations commonly used in logistics and transportation management systems.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-REST_API-black)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Marshmallow](https://img.shields.io/badge/Marshmallow-Validation-green)

---

## 🚀 Overview

Freight and logistics companies need a centralized system to manage shipment loads, allocate transportation resources, and track deliveries efficiently.

This API provides:

* Load creation and management
* Origin and destination tracking
* Truck allocation management
* Shipper identification
* Data validation
* Persistent storage
* RESTful CRUD operations

The service can act as the backend foundation for transportation management systems (TMS), freight marketplaces, and logistics platforms.

---

## ✨ Features

### 📦 Load Management

* Create shipment loads
* Retrieve individual shipments
* List all active loads
* Update shipment details
* Delete shipment records

### 🚛 Transportation Tracking

* Loading location tracking
* Unloading destination tracking
* Truck allocation management
* Weight and shipment capacity recording

### 📝 Data Validation

* Structured request validation
* JSON serialization and deserialization
* Schema-driven data integrity

### 🗄 Database Persistence

* SQLAlchemy ORM integration
* SQLite database storage
* Object-relational mapping
* Persistent shipment records

### 🔌 RESTful API Design

* Resource-oriented endpoints
* Standard HTTP methods
* Consistent JSON responses
* Proper status code handling

---

## 🏗 System Architecture

```text
Client (Postman / Frontend)
            │
            ▼
     Flask REST API
            │
            ▼
      Marshmallow
     Validation Layer
            │
            ▼
       SQLAlchemy
            │
            ▼
        SQLite DB
```

---

## 🛠 Technology Stack

| Layer             | Technology  |
| ----------------- | ----------- |
| Backend Framework | Flask       |
| ORM               | SQLAlchemy  |
| Serialization     | Marshmallow |
| Database          | SQLite      |
| API Testing       | Postman     |
| Language          | Python      |

---

## 📂 Project Structure

```text
freight-load-management-api/
│
├── app.py
├── models.py
├── schemas.py
├── requirements.txt
├── instance/
│   └── database.db
│
└── README.md
```

> Project structure may vary slightly depending on your implementation.

---

## ⚙️ Installation

### Prerequisites

Before running the project, ensure you have:

* Python 3.8+
* pip
* SQLite

---

### Clone Repository

```bash
git clone https://github.com/jv0019/Freight-Load-Management-REST-API.git
cd Freight-Load-Management-REST-API
```

---

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask server:

```bash
python -m flask run
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

## 📚 API Endpoints

### Create Load

**POST** `/load`

Creates a new shipment load.

#### Example Request

```json
{
  "loading_point": "Mumbai",
  "unloading_point": "Pune",
  "product_type": "Cement",
  "truck_type": "Heavy",
  "no_of_trucks": 3,
  "weight": 500.0,
  "shipper_id": "abc123",
  "date": "2026-03-06"
}
```

#### Success Response

```json
{
  "message": "Load created successfully"
}
```

---

### Retrieve All Loads

**GET** `/load`

Returns all shipment loads.

#### Example

```http
GET /load
```

---

### Retrieve Single Load

**GET** `/load/<load_id>`

Returns a specific shipment using its unique identifier.

#### Example

```http
GET /load/1
```

---

### Update Load

**PUT** `/load/<load_id>`

Updates an existing shipment record.

#### Example

```http
PUT /load/1
```

---

### Delete Load

**DELETE** `/load/<load_id>`

Deletes a shipment record.

#### Example

```http
DELETE /load/1
```

---

## 🗄 Database Design

### Load Model

The system stores freight shipment information including:

| Field           | Description                |
| --------------- | -------------------------- |
| loading_point   | Shipment origin            |
| unloading_point | Shipment destination       |
| product_type    | Type of cargo              |
| truck_type      | Vehicle category           |
| no_of_trucks    | Number of allocated trucks |
| weight          | Shipment weight            |
| shipper_id      | Unique shipper identifier  |
| date            | Shipment date              |

---

## 🔍 Request Validation

Marshmallow schemas are used for:

* Input validation
* JSON serialization
* Data deserialization
* Type checking
* Error reporting

This ensures consistent API behavior and protects against invalid payloads.

---

## ⚠ Error Handling

The API returns appropriate HTTP status codes and error messages.

### Common Status Codes

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | Success               |
| 201         | Resource Created      |
| 400         | Bad Request           |
| 404         | Resource Not Found    |
| 500         | Internal Server Error |

---

## 🧪 Testing

The API can be tested using:

* Postman
* Insomnia
* curl
* Any HTTP client

### Example

```bash
curl -X GET http://127.0.0.1:5000/load
```

---

## 💡 Learning Outcomes

This project demonstrates:

* REST API development
* CRUD operations
* Database design
* ORM usage with SQLAlchemy
* Request validation using Marshmallow
* Backend architecture principles
* JSON API design
* Logistics domain modeling

---

## 🚀 Future Improvements

* [ ] JWT Authentication
* [ ] User & Shipper Management
* [ ] PostgreSQL Support
* [ ] Pagination & Filtering
* [ ] Search Functionality
* [ ] API Documentation with Swagger/OpenAPI
* [ ] Shipment Status Tracking
* [ ] Rate Limiting
* [ ] Docker Deployment

---

## 📜 License

MIT License

---

## 👤 Author

**Jivitesh Sachdev**

Software Development • Backend Engineering • API Design

GitHub: https://github.com/jv0019

---

### Keywords

REST API • Flask • SQLAlchemy • Marshmallow • Logistics Software • Freight Management • Transportation Management System • Backend Development • CRUD API • Python
