from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books: list[Book] = []

# Add the endpoints described in README.md.
