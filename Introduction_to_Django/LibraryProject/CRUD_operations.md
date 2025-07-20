# CRUD Operations Using Django Shell

This section documents the create, retrieve, update, and delete operations on the `Book` model via the Django shell.

---

## Create a Book

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Retrieve book

book
# <Book: 1984 by George Orwell (1949)>

# Update the book title

book = Book.objects.get(title="1984")

print(book.title, book.author, book.publication_year)
# 1984 George Orwell 1949

book.title = "Nineteen Eighty-Four"
book.save()

book
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

# Delete the book
book.delete()
# (1, {'bookshelf.Book': 1})

Book.objects.all()
# <QuerySet []>

