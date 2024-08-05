listBook={
  "library": {
    "name": "My Book Library",
    "location": "123 Library Lane, Booktown, BK 12345",
    "books": [
      {
        "id": "1",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publishedYear": 1960,
        "genre": "Fiction",
        "isbn": "978-0061120084",
        "availableCopies": 3
      },
      {
        "id": "2",
        "title": "1984",
        "author": "George Orwell",
        "publishedYear": 1949,
        "genre": "Dystopian",
        "isbn": "978-0451524935",
        "availableCopies": 5
      },
      {
        "id": "3",
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "publishedYear": 1851,
        "genre": "Adventure",
        "isbn": "978-1503280786",
        "availableCopies": 2
      },
      {
        "id": "4",
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publishedYear": 1813,
        "genre": "Romance",
        "isbn": "978-1503290563",
        "availableCopies": 4
      }
    ]
  }
}

index=1
for i in listBook["library"]["books"]:
    print(index,"]",i["title"])
    index +=1
def showBooks():
    exit()
while False:
    print("1)show Book \n4)Exit \n" )
    selectChooice=int(input("select the option \n"))
    if selectChooice ==1:
        showBooks()
    elif selectChooice == 4:
        exit()
    else:
        print("Invalid Option Try Again \n")