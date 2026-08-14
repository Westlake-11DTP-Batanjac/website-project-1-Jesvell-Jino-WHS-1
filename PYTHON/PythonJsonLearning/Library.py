import json

books = [
    {
        "title" : "Lord of the Fries",
        "author" : "William Cumberbatch",
        "year" : 1974,
        "rating" : 5
    },
    {
        "title" : "Fries of Lies of P",
        "author" : "Bengamin Frankling",
        "year" : 2004,
        "rating" : 2
    },
    {
        "title" : "Kuhutantian",
        "author" : "Kantian Kamhir",
        "year" : 321,
        "rating" : 4
    },

]

with open("librarystore.json", "w") as file:
    json.dump(books, file, indent=2)