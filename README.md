# Theatre-api

About
Theatre API is a RESTful web service for online seat booking in theaters across your city.

## Installation & Setup

**Clone the repo**  
   ```bash
   git clone https://github.com/ALEX09051981/theatre-api.git
   cd theatre-api
```
  
##  Tech Stack

- **Language:** Python 3.11+
- **Framework:** Django 4.x, Django REST Framework
- **Auth:** djangorestframework-simplejwt
- **Docs:** drf-spectacular (OpenAPI 3)
- **Database:** PostgreSQL (SQLite for tests)
- **Containerization:** Docker, Docker Compose
- **Linting:** flake8, ruff
- **Formatting:** black
- **Testing:** Django TestCase, DRF APIClient, pytest (optional)


## Testing

Run all tests
```bash
docker-compose exec web python manage.py test
```

## API Documentation

* Swagger UI:
http://127.0.0.1:8000/api/doc/swagger/

* Redoc:
http://127.0.0.1:8000/api/doc/redoc/


##API Features
* JWT Authentication:

Obtain, refresh, and blacklist access tokens using djangorestframework-simplejwt.

* User Management

Custom user model (AbstractUser)

Registration and profile endpoints

Admin-only access for certain operations

*  Play Management

Create, retrieve, update, delete plays

Attach genres and actors to plays

*  Theatre Hall Management

Define halls with rows and seats

Full CRUD support

*  Session Management

Schedule movie/play sessions in specific halls

Associate sessions with a play and time

* Reservation System

Reserve specific seats for a session

Prevent double-booking of the same seat

Automatically associate reservations with users

* Ticketing & Orders

Users can place orders and receive tickets

Order history and ticket detail views

Admin access to all orders

* Search & Filtering

Search by play title, actor, genre

Filter sessions by play or date

Filter available seats

* API Documentation

Swagger UI and Redoc auto-generated from OpenAPI schema (drf-spectacular)

* Docker Support

Fully containerized with PostgreSQL and Redis support
