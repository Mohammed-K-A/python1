# Admin credentials
admins = {"admin": "admin123"}

# Book and User storage
books = {}
users = {}

# Function to display all books
def display_books():
    if not books:
        print("No books available.")
    else:
        for book_id, details in books.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Qty: {details['quantity']}")

# Main menu
while True:
    print("\n1. Admin\n2. User\n3. Exit")
    choice = input("Select option: ")

    if choice == '1':
        # Admin Login
        uname = input("Enter admin username: ")
        pwd = input("Enter admin password: ")

        if admins.get(uname) == pwd:
            while True:
                print("\n--- Admin Menu ---")
                print("1. Add Book\n2. Update Book\n3. Delete Book\n4. Display All Books\n5. Logout")
                a_choice = input("Choose: ")

                if a_choice == '1':
                    book_id = input("Enter Book ID: ")
                    title = input("Enter Title: ")
                    author = input("Enter Author: ")
                    quantity = int(input("Enter Quantity: "))
                    books[book_id] = {"title": title, "author": author, "quantity": quantity}
                    print("Book added.")
                
                elif a_choice == '2':
                    book_id = input("Enter Book ID to update: ")
                    if book_id in books:
                        title = input("New Title: ")
                        author = input("New Author: ")
                        quantity = int(input("New Quantity: "))
                        books[book_id] = {"title": title, "author": author, "quantity": quantity}
                        print("Book updated.")
                    else:
                        print("Book not found.")

                elif a_choice == '3':
                    book_id = input("Enter Book ID to delete: ")
                    if books.pop(book_id, None):
                        print("Book deleted.")
                    else:
                        print("Book not found.")

                elif a_choice == '4':
                    display_books()

                elif a_choice == '5':
                    break
                else:
                    print("Invalid choice.")

        else:
            print("Invalid admin credentials.")

    elif choice == '2':
        print("\n1. Register\n2. Login")
        u_choice = input("Select: ")

        if u_choice == '1':
            phone = input("Phone (unique): ")
            if phone in users:
                print("Phone already registered.")
            else:
                name = input("Name: ")
                age = input("Age: ")
                address = input("Address: ")
                username = input("Username (unique): ")
                password = input("Password: ")
                users[phone] = {"name": name, "age": age, "address": address, "username": username, "password": password}
                print("Registered successfully.")

        elif u_choice == '2':
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            found = False
            for user in users.values():
                if user["username"] == uname and user["password"] == pwd:
                    found = True
                    while True:
                        print("\n--- User Menu ---")
                        print("1. Display All Books\n2. Search Book by Name\n3. Logout")
                        u_opt = input("Choose: ")

                        if u_opt == '1':
                            display_books()

                        elif u_opt == '2':
                            search_title = input("Enter title to search: ").lower()
                            found_books = [book for book in books.values() if search_title in book['title'].lower()]
                            if found_books:
                                for book in found_books:
                                    print(book)
                            else:
                                print("No books found.")

                        elif u_opt == '3':
                            break
                        else:
                            print("Invalid option.")
                    break

            if not found:
                print("Invalid login credentials.")

    elif choice == '3':
        print("Exiting the system.")
        break

    else:
        print("Invalid input.")















        # if login_username in user and user[login_username]["password"] == login_password:
        #         print(f"Welcome, {user[login_username]['name']}!")
        #         while True:
        #             print("1. Display All Books")
        #             print("2. Search Book by Title")
        #             print("3. Exit")

        #             user_choice = int(input("Enter your choice: "))

        #             if user_choice == 1:
        #                 if book:
        #                     for bid, info in book.items():
        #                         print(f"ID: {bid}, Title: {info['title']}, Author: {info['author']}, Quantity: {info['quantity']}")
        #                 else:
        #                     print("No books available.")

        #             elif user_choice == 2:
        #                 search_title = input("Enter the book title to search: ").lower()
        #                 found = False
        #                 for b in book.values():
        #                     if b["title"].lower() == search_title:
        #                         print(f"Title: {b['title']}, Author: {b['author']}, Quantity: {b['quantity']}")
        #                         found = True
        #                 if not found:
        #                     print("Book not found.")

        #             elif user_choice == 3:
        #                 break
        #             else:
        #                 print("Invalid choice.")

