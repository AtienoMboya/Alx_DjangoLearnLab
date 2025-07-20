# Delete Operation

## Command

```python
from bookshelf.models import Book"
book.delete()
# (1, {'bookshelf.Book': 1})

Book.objects.all()
# <QuerySet []>
```

## Expected Output

```
(1, {'bookshelf.Book': 1})
<QuerySet []>
```
