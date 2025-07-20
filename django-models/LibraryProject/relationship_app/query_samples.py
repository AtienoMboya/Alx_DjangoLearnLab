from relationship_app.models import Author, Book, Library, Librarian

# --- Query 1: All books by a specific author ---
author_name = "George Orwell"

try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# --- Query 2: All books in a library ---
library_name = "Central Library"

try:
    library = Library.objects.get(name=library_name)  # <- Required line
    books_in_library = library.books.all()
    print(f"\nBooks in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# --- Query 3: Retrieve the librarian for a library ---
try:
    library = Library.objects.get(name=library_name)  # <- Required line
    librarian = library.librarian
    print(f"\nLibrarian for {library.name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}")
