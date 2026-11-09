# 📘 Assignment: Web Interface for a REST API

## 🎯 Objective

Build a browser-based interface for the book catalog API from the FastAPI assignment. Practice connecting an HTML page to an API with JavaScript `fetch` requests and using HTTP methods to manage data.

## 📝 Tasks

### 🛠️ Prepare the API for a Browser Client

#### Description
Use your completed book catalog API and allow a local browser page to make requests to it. The API and web page run on different local ports, so the API must allow the page's origin.

#### Requirements
Completed program should:

- Add FastAPI's `CORSMiddleware` to the book catalog application.
- Allow the origin `http://localhost:5500` and the `GET`, `POST`, `PUT`, and `DELETE` methods.
- Start the API with `uvicorn starter-code:app --reload` from the API assignment directory.
- Serve this assignment's `index.html` from its directory with `python -m http.server 5500`.


### 🛠️ Display and Add Books

#### Description
Complete the browser page so it loads books from the API and lets a user add a book. Use the form and list scaffold in `index.html`.

#### Requirements
Completed program should:

- Send a `GET` request to `http://localhost:8000/books` and display each book's ID, title, and author.
- Submit the form as JSON to `POST /books`, including an integer `id`, `title`, and `author`.
- Refresh the displayed list after a book is added.
- Show a useful message when a request fails.


### 🛠️ Edit and Remove Books

#### Description
Add controls for each displayed book so a user can update its details or remove it from the catalog.

#### Requirements
Completed program should:

- Let the user select a book to edit and submit its changed details with `PUT /books/{book_id}`.
- Send a `DELETE /books/{book_id}` request when a user chooses to remove a book.
- Refresh the displayed list after a successful update or removal.
- Keep the book's ID consistent between the selected book and the API request.