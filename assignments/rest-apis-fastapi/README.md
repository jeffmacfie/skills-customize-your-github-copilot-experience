# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing a small book catalog with FastAPI. Practice defining routes, handling HTTP methods, validating request data, and returning appropriate responses.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Set up the FastAPI application and add a health-check endpoint so a client can confirm that the API is running.

#### Requirements
Completed program should:

- Use the FastAPI application scaffold in `starter-code.py`.
- Define a `GET /health` endpoint.
- Return `{"status": "ok"}` from the health endpoint.
- Install FastAPI and Uvicorn, then start the application with `uvicorn starter-code:app --reload`.
- Confirm the health endpoint responds.


### 🛠️ Add Book Listing and Creation

#### Description
Represent books with a Pydantic model, then add endpoints to list books and add a book to the in-memory catalog.

#### Requirements
Completed program should:

- Define a book model with an integer `id`, a `title`, and an `author`.
- Define `GET /books` to return all books in the catalog.
- Define `POST /books` to accept a book and add it to the catalog.
- Return the newly created book from `POST /books` with HTTP status `201 Created`.


### 🛠️ Retrieve, Update, and Delete Books

#### Description
Add endpoints that let a client retrieve one book by its ID, replace its details, and remove it from the catalog.

#### Requirements
Completed program should:

- Define `GET /books/{book_id}` to return the matching book.
- Define `PUT /books/{book_id}` to replace the matching book's details.
- Define `DELETE /books/{book_id}` to remove the matching book.
- Return HTTP status `404 Not Found` when a requested book ID does not exist.
- Test each endpoint using the interactive API documentation at `/docs`.
