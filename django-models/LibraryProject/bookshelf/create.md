# Create Operation

## Command

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

## Expected Output

A `Book` instance is created and returned as:
```
<Book: 1984 by George Orwell (1949)>
```
