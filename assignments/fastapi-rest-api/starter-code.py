from typing import Dict, List

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


class Book(BookCreate):
    id: int


books: Dict[int, Book] = {}
next_book_id = 1


@app.get("/books", response_model=List[Book])
def list_books():
    # TODO: Retorne todos os livros cadastrados.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Busque o livro pelo ID ou responda com HTTP 404.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    global next_book_id

    # TODO: Crie o livro, atribua um ID, salve-o em books e incremente next_book_id.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate):
    # TODO: Atualize o livro pelo ID ou responda com HTTP 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    # TODO: Exclua o livro pelo ID ou responda com HTTP 404.
    # Retorne uma resposta vazia com status HTTP 204.
    pass