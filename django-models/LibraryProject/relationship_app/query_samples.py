from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}:", list(books_by_author))

# List all books in a library
library = Library.objects.get(name="City Library")
books_in_library = library.books.all()
print(f"Books in {library.name}:", list(books_in_library))

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian of {library.name}:", librarian.name)
