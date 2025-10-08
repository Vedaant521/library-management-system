def add_Book():
    title = input("Enter title of book:")
    author = input("Enter author name of book:")
    price = input("Enter price of book:")
    with open("Library.txt","a")as f:
        f.write(f"{title},{author},{price}\n")
        print("Book is added successfully")

def view_Book():
    print("Library management...>>>!!!")
    with open("Library.txt","r")as f:
        Lines = f.readlines()
        print("Title|Author|Price")
        for line in Lines:
            data = line.strip().split(",")
            print(f"{data[0]}|{data[1]}|{data[2]}")
        
def search_Book():     
    print("Library management...>>>!!!")
    t = input("Enter title of book you want to seaarch in library:")
    found = False
    with open("Library.txt","r")as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(",")
            if(t.lower() == data[0].lower()):
                found = True
                print(f"{data[0]}|{data[1]}|{data[2]}")
                break            
    if not found:
        print("Invalid")

def delete_Book():
    print("Library management....>>>!!!")
    t = input("Enter title of book you want to delete:")
    found = False
    new_line = []
    with open("Library.txt","r")as f:
        Lines = f.readlines()
        for line in Lines:
            data = line.strip().split(",")
            if(t.lower() == data[0].lower()):
                found = True
                print(f"Deleted {data[0]}|{data[1]}|{data[2]}")
            else:
                 new_line.append(line)
    if found:
        with open("Library.txt","w")as f:
            f.writelines(new_line)
        print("Book is deleted successfully...!!!")
    else:
        print("File not found")     

def update_Book():
    title = input("Enter the title of book for update:")
    found = False
    new_lines = []
    with open("Library.txt","r")as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(",")
            if(title.lower() == data[0].lower()):
                found = True
                print(f"Updation of old record{data[0]}|{data[1]}|{data[2]}")
                new_title = input("Enter new title:")
                new_author = input("Enter new author:")
                new_price = input("Enter new price:")
                new_lines.append(f"{new_title}|{new_author}|{new_price}\n")
            else:
                new_lines.append(line)
    if found:
        with open("Library.txt","w")as f:
             f.writelines(new_lines)
             print("Book record updated successfully")
    else:
        print("Book not found..!")
        
    
while True:
    print("Library management...>>>!!!")
    print("Enter 1 for to add_Book")
    print("Enter 2 for view Library_Book")
    print("Enter 3 for search_Book")
    print("Enter 4 for delete_Book")
    print("Enter 5 for update_book")
    print("Enter 6 for end of program")
    choice = input("Enter your choice:")
    if(choice == "1"):
        add_Book()
    elif(choice == "2"):
        view_Book()
    elif(choice == "3"):
        search_Book()
    elif(choice == "4"):
        delete_Book()    
    elif(choice == "5"):
        update_Book()
    elif(choice == "6"):
        print("end program")
        break
    else:
        print("Invalid choice") 
