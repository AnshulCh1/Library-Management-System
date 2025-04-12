from curd import add_book, get_book, add_memb

def add_new_book():
    title = input("Enter the Name of the Book: ")
    author = input("Enter the name of Author: ")
    isbn = input("Enter Book's ISBN: ")
    count = input("Enter copies of Books: ")
    add_book(title, author, isbn, count)

def print_book():
    books= get_book()
    for book in books:
        available= "available" if book .count > 0 else "Not available"
        print(f"{book.id}: '{book.title}' by {book.author} (ISBN: {book.isbn}) - {book.count} copies")

def add_new_memb():
    name = input("Enter members name: ")
    email = input("Enter Email: ")
    add_memb(name, email)

def print_memb():
    pass

    
def main():
    print("*******************************************")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Member")
    print("4. View Member")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. View Transanctions")
    print("*******************************************")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_new_book()

    elif choice == "2":
        print_book()

    elif choice == "3":
        add_new_memb()

    elif choice == "4":
        pass

    elif choice == "5":
        pass

    elif choice == "6":
        pass

    elif choice == "7":
        pass    

if __name__ == "__main__":
    main()


    