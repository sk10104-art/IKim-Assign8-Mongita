from mongita import MongitaClientDisk
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
client = MongitaClientDisk(os.path.join(BASE_DIR, "mongita_data"))
db = client.bookstore
categories_col = db.category
books_col = db.book

# Reset collections
categories_col.delete_many({})
books_col.delete_many({})

# -----------------------------
# CATEGORIES (4 required)
# -----------------------------
categories_col.insert_many([
    {"categoryId": 1, "categoryName": "Biographies"},
    {"categoryId": 2, "categoryName": "Learn to Play"},
    {"categoryId": 3, "categoryName": "Music Theory"},
    {"categoryId": 4, "categoryName": "Scores and Charts"}
])

# -----------------------------
# BOOKS (at least 6 required - we have 8)
# -----------------------------
books_col.insert_many([
    {
        "bookId": 1, "categoryId": 1, "categoryName": "Biographies",
        "title": "Beethoven", "author": "David Jacobs",
        "isbn": "13-9780304936588", "price": 9.99,
        "image": "beethoven.gif", "readNow": 0
    },
    {
        "bookId": 2, "categoryId": 1, "categoryName": "Biographies",
        "title": "Madonna", "author": "Andrew Morton",
        "isbn": "13-9780312287863", "price": 12.99,
        "image": "madonna.jpg", "readNow": 1
    },
    {
        "bookId": 3, "categoryId": 1, "categoryName": "Biographies",
        "title": "Clapton: The Autobiography", "author": "Eric Clapton",
        "isbn": "13-9780767925365", "price": 10.99,
        "image": "clapton.jpg", "readNow": 1
    },
    {
        "bookId": 4, "categoryId": 1, "categoryName": "Biographies",
        "title": "Music is My Mistress", "author": "Edward Kennedy Ellington",
        "isbn": "13-9780303608037", "price": 68.99,
        "image": "ellington.jpg", "readNow": 0
    },
    {
        "bookId": 5, "categoryId": 2, "categoryName": "Learn to Play",
        "title": "Play Piano Today!", "author": "Hal Leonard",
        "isbn": "13-9780634069321", "price": 19.99,
        "image": "piano.jpg", "readNow": 1
    },
    {
        "bookId": 6, "categoryId": 2, "categoryName": "Learn to Play",
        "title": "Guitar Basics", "author": "James Longworth",
        "isbn": "13-9780571538163", "price": 14.99,
        "image": "guitar.jpg", "readNow": 0
    },
    {
        "bookId": 7, "categoryId": 3, "categoryName": "Music Theory",
        "title": "Music Theory Essentials", "author": "Jason W. Solomon",
        "isbn": "13-9781423492724", "price": 21.95,
        "image": "theory.jpg", "readNow": 1
    },
    {
        "bookId": 8, "categoryId": 4, "categoryName": "Scores and Charts",
        "title": "Classical Favorites", "author": "Various",
        "isbn": "13-9780793512737", "price": 15.99,
        "image": "scores.jpg", "readNow": 0
    }
])

print("Bookstore Mongita DB created.")

# -----------------------------
# JSON EXPORTS (required by assignment)
# -----------------------------
def clean_doc(doc):
    """Remove Mongita's internal _id field for clean JSON."""
    doc.pop("_id", None)
    return doc

categories_data = [clean_doc(c) for c in categories_col.find()]
books_data = [clean_doc(b) for b in books_col.find()]

with open(os.path.join(BASE_DIR, "categories.json"), "w") as f:
    json.dump(categories_data, f, indent=2)

with open(os.path.join(BASE_DIR, "books.json"), "w") as f:
    json.dump(books_data, f, indent=2)

print("Exported categories.json and books.json")
