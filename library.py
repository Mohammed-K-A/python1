admins = {"username":"mohammed","password":"password"}
user = {}
book = {}

while True:
    print("1.Admin")
    print("2.User")
    option=int(input("Choose 1 or 2:"))

    if option==1:
        a_name=input("Enter the username:")
        a_password=input("Enter the password:")

        if a_name in admins["username"] and a_password in admins["password"]:
            while True:
                print("1.Add Book")
                print("2.Update Book")
                print("3.Delete Book")
                print("4.Display All Book")
                print("5.Exit")

                option2=int(input("Enter a choice:"))
                if option2==1:
                    book_id=input("Enter a book id :")
                    if book_id in book:
                        print("Book already exists")
                    else:
                        title=input("Enter a title:")
                        author=input("Enter the author:")
                        quantity=int(input("Enter the quantity:"))
                        book[book_id]={"title":title,"author":author,"quantity":quantity}

                        print("Book Added Successfully")
                elif option2==2:
                    book_id=input("Enter a book id:")
                    if book_id in book:
                        book[book_id]['title']=input("Enter updated title: ")
                        book[book_id]['author']=input("Enter updated author: ")
                        book[book_id]['qty']=input("Enter updated quantity: ")
                        print("Book Updated Successfully")
                    else:
                        print("Book Id Does Not Exist")

                elif option2==3:
                    book_id=input("Enter a book id:")
                    if book_id in book:
                        del book[book_id]
                        print("Book Deleted Successfully")
                    else:
                        print("Book Id Does Not Exist")
                
                elif option2==4:
                    print(book)
                
                elif option2==5:
                    print("exit")
                    break
                else:
                    print("Invalid choice")
                    break

    elif option==2:
       while True: 
        print("1.Registration")        
        print("2.Login")        
            
        option=int(input("Enter the choice:"))
        if option==1:
            u_name=input("Enter Your Name: ")
            u_age=int(input("Enter Your Age: "))
            u_address=input("Enter the Address: ")
            u_phone_no=int(input("Enter Contact no (unique): "))
            u_username=input("Create an Username (unique): ")
            u_password=input("Create a Password: ")
            
            if u_username in user:
                print("Username already exists")
            
            elif u_phone_no in user:
                print("Phone Number already exists")

            else:
                user[u_username]={"name": u_name,"age": u_age,"address": u_address,"phone_number": u_phone_no,"password": u_password}
                print("Registration Successful")

        elif option==2:
            login_username=input("Enter your username: ")
            login_password=input("Enter your password: ")

            if login_username in user and user[login_username]["password"]==login_password:
                while True:
                    print("1.Display All Books")
                    print("2.Search Book by Title")
                    print("3.Exit")

                    user_choice=int(input("Enter the choice: "))

                    if user_choice==1:
                        if book:
                            print(book)
                        else:
                            print("Books does not exist")
                    
                    elif user_choice==2:
                        search=input("Enter the book title: ")
                        if search in title:
                            print(book)
                        else:
                            print("Invalid title")
                    
                    elif user_choice==3:
                        print("exit")
                        break
                        
                    else:
                        print("Invalid choice")
                        break
            else:
                print("User not found")

    else:
        print("Invalid Credentials")
                        
                

                

       
            

