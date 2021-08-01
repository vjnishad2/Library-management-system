class library:
    def __init__(self,book):
        self.book= book

    def listofbooks(self):
        print(f"List of book are {self.book}")
        for book in self.book:
            print("@" + book)

    def borrowBook(self,book):
        if book in self.book:
            print("Book has been issued to you")
            self.book.remove(book)
        else:
            print("Sorry.....Book is not available")
            return True

    def returnBook(self,bookName):
        self.book.append(bookName)
        print("Thanks for returning")


class student:
    def borrowBook(self):
        self.book = input("Enter the book you want")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book to return")
        return self.book

if __name__== "__main__":  
        centraLibrary = library(["Algorithms", "Django", "Clrs", "Python Notes"])
        student = student()
        while(True):
            welcomeMsg = '''\n ====== Welcome to Central Library ======
            Please choose an option:
            1. List all the books
            2. Request a book
            3. Add/Return a book
            4. Exit the Library
            '''
            print(welcomeMsg)
            a = int(input("Enter your choice"))
            if a == 1:
                centraLibrary.listofbooks()
            elif a == 2:
                centraLibrary.borrowBook(student.borrowBook())
            elif a==3:
                centraLibrary.returnBook(student.returnBook())
            elif a ==4:
                print("Thank you")
                exit()
            else:
                print("Invalid choice")
