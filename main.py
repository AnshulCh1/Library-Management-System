from curd import add_book, get_book, add_memb, get_memb, issue_book, return_book, transaction_for_member

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
    members = get_memb()
    for member in members:
        print(f"{member.id}. {member.name} (Email: {member.email})")

def issue_new_book():
    book_id = int(input("Enter book id: "))
    member_id =int(input("Enter member id: "))
    issue_book(book_id, member_id)   

def return__book():
    transaction_id = int((input("Enter the Tranction ID: ")))
    return_book(transaction_id)

def get_transaction_for_member():
    member_id = int(input("Enter Member ID: "))
    transactions = transaction_for_member(member_id)
    for transaction in transactions:
        return_state = "Returned" if transaction.return_date else "Not returned"
        print(f"Transaction ID: {transaction.id} , Book ID: {transaction.book_id}, Member ID: {transaction.member_id}, Issue Date: {transaction.issue_date}, Return Date: {transaction.return_date}, Return Status: {return_state}")
    print("--------------")

def main():
    while True:  # for continuing the program 
        
        print("*******************************************")
        print("*******************************************") 
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Member")
        print("4. View Member")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. View Transanctions")
        print("8. Exit")
        print("*******************************************")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_book()

        elif choice == "2":
            print_book()

        elif choice == "3":
            add_new_memb()

        elif choice == "4":
            print_memb()

        elif choice == "5":
            issue_new_book()

        elif choice == "6":
            return__book()

        elif choice == "7":
            get_transaction_for_member()  

        else:
            break     

if __name__ == "__main__":
    main()


    