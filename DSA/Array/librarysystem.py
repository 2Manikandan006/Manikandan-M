class Library_system:
    def add_book(self, books):
        self.book = []
        for i in range(books): 
            book = input(f"Enter the name of the book {i+1} : ")    
            self.book.append(book)

    def display_books(self):
        print("The books are available in the list are : ")
        for book in self.book:
            print(book)

    def search_book(self, book):
        if book in self.book:
            index = self.book.index(book)
            print(f"The searched book is : {book} at position {index + 1}")
        else:
            print(f"The book {book} is not available in the library")

    def update_book(self, book):
        if book in self.book:
            index = self.book.index(book)
            new_book = input("Enter the name of the book to be updated with the current book : ")
            self.book[index] = new_book
            print(f"The book {book} is updated to the library")
        else:
            print(f"The book {book} is not available in the library")

if __name__ == "__main__":
    library = Library_system()

    while True:

        print("\n1. Add a new book ")
        print("2. Display books")
        print("3. Search a book ")
        print("4. Update the book ")
        print("5. Exit ")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            books = int(input("Enter the number of books to be added : "))
            library.add_book(books)

        elif choice == 2:
            library.display_books()
        
        elif choice == 3:
            book = input("Enter the name of the book to be searched : ")
            library.search_book(book)

        elif choice == 4:
            book = input("Enter the name of the book in the library to be update : ")
            library.update_book(book)

        elif choice == 5:
            print("Exiting... Thankyou!. ")
            break
        else:
            print("Invalid input! please try again.")