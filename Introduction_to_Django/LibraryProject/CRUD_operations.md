# CRUD Operations for Book Model

This file documents create, retrieve, update, and delete operations on the `Book` model using Django ORM via the shell.

---

## Create

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book
# <Book: 1984 by George Orwell (1949)>
```

---

## Retrieve

```python
book = Book.objects.get(title="1984")

print(book.title, book.author, book.publication_year)
# 1984 George Orwell 1949
```

---

## Update

```python
book.title = "Nineteen Eighty-Four"
book.save()

book
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
```

---

## Delete

```python
book.delete()
# (1, {'bookshelf.Book': 1})

Book.objects.all()
# <QuerySet []>
```
