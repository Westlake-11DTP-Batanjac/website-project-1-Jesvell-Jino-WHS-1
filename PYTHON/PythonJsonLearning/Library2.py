import json

with open("librarystore.json", "r") as file:
    books = json.load(file)

for i in range(len(books)):
    title = books[i]["title"]
    author = books[i]["author"]
    rating = books[i]["rating"]
    print(f"{title} by {author} - {rating}/5")

def average_rating(book):
    sum = 0
    for i in range(len(book)):
        sum += book[i]["rating"]
    avg = sum / len(book)
    return avg

print("Average rating is",average_rating(books))