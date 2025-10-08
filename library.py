'''
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def show_book(self):
        print("Title|Author|Price")
        print(f"{self.title}|{self.author}|{self.price}")
class library:
    def add_Book(self):
        title = input("Enter title:")
        author = input("Enter author name:")
        price = input("Enter price of book:")
        book = Book(title,author,price)
        with open("Book.txt","a")as f:
            f.write(f"{book.title}|{book.author}|{book.price}\n")
        print("Book is added successfully...!!!")
        book.show_book()
    
    def view_Book(self):
        print("Library management...!!!")
        with open("Book.txt","r")as f:
            lines = f.readlines()
            print("Title|Author|price")
            for line in lines:
                data = line.strip().split("|")
                print(f"{data[0]}|{data[1]}|{data[2]}")
    def delete_Book(self):
        t = input("Enter title:")
        found = False
        new_lines = []
        with open("Book.txt","r")as f:
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|")
                if(data[0] == t):
                    found = True
                    print(f"Deleted{data[0]}|{data[1]}|{data[2]}")
                else:
                   new_lines.append(lines)
        if found:
            with open("Book.txt","w")as f:
                f.writelines(new_lines)
            print("Book is deleted successfully...!")
        else:
            print("Invalid book")
    def update_Book(self):
        print("Library management...!!!")
        t = input("Enter title of book you want to update in library:")
        found = False
        new_lines = []
        with open("Book.txt","r")as f:
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|")
                if(data[0].lower() == t.lower()):
                    found = True
                    print(f"Updation of old record:{data[0]}|{data[1]}|{data[2]}")
                    new_title = input("Enter new title for book:")
                    new_author = input("Enter author name for book:")
                    new_price = input("Enter new price for book:")
                    new_lines.append(f"{new_title}|{new_author}|{new_price}\n")
                else:
                    new_lines.append(line)
        if found:
            with open("Book.txt","w")as f:
                f.writelines(new_lines)
                print("Book is updated successfully...!!!")
        else:
            print("Invalid book")


library = library()
while True:
    print("Library management...>>>")
    print("Enter 1 for add_book")
    print("Enter 2 for view_book")
    print("Enter 3 for delete_book")
    print("Enter 4 for update_book")
    choice = input("Enter choice:")
    if(choice == "1"):
        library.add_Book()
    elif(choice == "2"):
        library.view_Book()
    elif(choice == "3"):
        library.delete_Book()    
    elif(choice == "4"):
        library.update_Book()    
        break
    else:
        print("Invalid book")'''

class Book:
    def __init__(self,author,title,price):
        self.title = title
        self.author = author
        self.price = price
    def show(self):
        print("Library Management System....>>>")
        print("Title|Author|Price")
        print(f"{self.title}|{self.author}|{self.price}\n")
class Library(Book):
    def add_book(self):
        print("Library Management System...>>>")
        self.title = input("Enter Book title:")
        self.author = input("Enter Author name:")
        self.price = input("Enter book price:")
        with open("library2.txt","a")as f:
            f.write(f"{self.title}|{self.author}|{self.price}\n")
        print("Book added successfully..>>>")      
        self.show()

    def view_book(self):
        print("Library management system...>>>")
        with open("library2.txt","r")as f:
            lines = f.readlines()
            print("Title|Author|Price")
            for line in lines:
                data = line.strip().split("|")
                print(f"{data[0]}|{data[1]}|{data[2]}\n")

    def update_book(self):
        title = input("Enter book title you want to update:")
        found = False
        update_lines =[]
        with open("library2.txt","r")as f:
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|") 
                if(data[0].lower() == title.lower()):
                    found = True
                    print(f"Updation of old record:{data[0]}|{data[1]}|{data[2]}")           
                    new_title = input("Enter new title of book:")
                    new_author = input("Enter new author of book:")
                    new_price = input("Enter new price of book:")
                    update_lines.append(f"{new_title}|{new_author}|{new_price}\n")
                else:
                    update_lines.append(line)
        if found:
            with open("library2.txt","w")as f:
                f.writelines(update_lines)
            print("Book details updated successfully...>>>")
        else:
            print("Invalid title...!!!")

    def delete_book(self):
        title = input("Enter book title you want to delete:")
        found = False
        update_lines = []
        with open("library2.txt","r")as f:
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|")
                if(data[0].lower()== title.lower()):
                    found = True
                    print(f"Deleted: {data[0]}|{data[1]}|{data[2]}\n")
                else:
                    update_lines.append(line)
        if found:
            with open("library2.txt","w")as f:
                f.writelines(update_lines)
            print("Book deleted successfully..>>>")
        else:
            print("Invalid book")

l = Library("","","")
while True:
    print("Library Management System..>>>")
    print("\\Library Menu..\\")
    print("Enter 1 for add book:")
    print("Enter 2 for view book:")
    print("Enter 3 for update book:")
    print("Enter 4 for delete book:")
    print("Enter 5 for exit:")
    choice = int(input("Enter your choice:"))
    if(choice == 1):
        l.add_book()
        l.show()
    elif(choice == 2):
        l.view_book()
    elif(choice == 3):
        l.update_book()
    elif(choice == 4):
        l.delete_book()
    elif(choice == 5):
        break
    else:
        print("Invalid choice")
