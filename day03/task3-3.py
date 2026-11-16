library = {
    "B001": {"title": "Python Programming", "author": "John Smith", "copies": 5},
    "B002": {"title": "Data Science 101", "author": "Alice Johnson", "copies": 3},
    "B003": {"title": "Web Development", "author": "Bob Brown", "copies": 2}
}

print("Library before issuing a book:")
print(library)

book_id_to_issue = "B001"
if library[book_id_to_issue]["copies"] > 0:
    library[book_id_to_issue]["copies"] -= 1

print("\nLibrary after issuing book B001:")
print(library)