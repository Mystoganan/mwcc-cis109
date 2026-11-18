#Dictionary
"""
[{
    "Key1": Value1,
    "Key2": {
        "Key3": Value3,
    }
}, {
    "Key4": Value4,
    "Key5":{
        "Key6":[Value6,Value7]
    }
}]
"""

books = []

book = {
    "author": "Charles Dickens",
    "title": "Great Expectations"
}

print(f"Author: {book["author"]}")

books.append(book)

book = {
    "author": "Dr.Suess",
    "title": "Green Eggs and Ham"
}

books.append(book)

print(f"Books List: {books}")
"""
for book in books:
    print(book)
"""
print(f"First Book's Author: {books[0]["author"]}")