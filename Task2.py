from datetime import date

class Library:
    def __init__(self, name, books, authors):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def __repr__(self):
        books_info = ''
        for book in self.books:
            books_info += repr(book) + "\n"

        authors_info = ''
        for author in self.authors:
            authors_info += repr(author) + "\n"

        return (f"Library name: {self.name}\nBooks: [\n{books_info}]\nAuthors: [\n{authors_info}]")

    def group_by_author(self, author):
        books_author = []
        for book in self.books:
            if book.author == author:
                books_author.append(book)
        return books_author

    def group_by_year(self, year):
        books_year = []
        for book in self.books:
            if book.year == year:
                books_year.append(book)
        return books_year


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.count = 3 # кількість екземплярів

    def __repr__(self):
        return (f"{self.name}, {self.year},  {repr(self.author)}, {self.count}")

class Author:
    def __init__(self, name, country, birthday, books = []):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books
    def __repr__(self):
        return (f"Author: [{self.name}, {self.country},  {self.birthday}]")

Hans_Christian_Andersen = Author("Hans_Christian_Andersen", "Denmark", date(1805, 4, 2), [])
Die_Gebrüder_Grimm = Author("Die_Gebrüder_Grimm", "Germany", date(1785, 1, 4), [])

Den_Lille_Havfrue = Book("Den_Lille_Havfrue", 1837, Hans_Christian_Andersen)
Rapunzel = Book("Rapunzel", 1812, Die_Gebrüder_Grimm)

library = Library("Tales", [Den_Lille_Havfrue, Rapunzel], [Hans_Christian_Andersen, Die_Gebrüder_Grimm])
library.new_book("Den_grimme", 1843, Hans_Christian_Andersen)
library.group_by_author(Hans_Christian_Andersen)
library.group_by_year(1843)

print(repr(library))