import datetime
import os
if not os.path.exists("library2.txt"):
    open("library2.txt","w").close()
if not os.path.exists("Issue_book.txt"):
    open("Issue_book.txt","w").close()
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
    def issue_book(self):
        print("//Library issue management..>>>")
        student_name = input("Enter student name:")
        title = input("Enter title of book to issue:")
        found = False
        with open("library2.txt","r")as f:
            for line in f:
                data = line.strip().split("|")
                if(data[0].lower() == title.lower()):
                    found = True
                    break
        if not found:
            print("Book not found in library..")
            return
        
        issue_date = datetime.date.today().strftime("%d-%m-%Y")
        with open("Issue_book.txt","a")as f:
            f.write(f"{title}|{student_name}|{issue_date}|Not Returned\n")
        print(f"Book {title} issued to {student_name} on {issue_date}")

    def return_book(self):
        print("//Library Management>>>")
        title = input("Enter book title you want to return:")
        student_name = input("Enter student name:")
        found = False
        update_lines = []
        with open("Issue_book.txt","r")as f:
            lines = f.readlines()
            for line in lines:
                data = line.strip().split("|")
                if(len(data)>=4 and data[0].lower()==title.lower() and data[1].lower()==student_name.lower() and "Not Returned" in data[3]):
                    found = True
                    return_date = datetime.date.today().strftime("%d-%m-%Y")
                    update_lines.append(f"{data[0]}|{data[1]}|{data[2]}|Returned on {return_date}\n")
                else:
                    update_lines.append(line)
        if found:
            with open("Issue_book.txt","w")as f:
                f.writelines(update_lines)
            print("Book returned successfully...>>>")
        else:
            print("No record found for this issue...!")

l = Library("","","")
while True:
    print("Library Management System..>>>")
    print("\\Library Menu..\\")
    print("Enter 1 for add book:")
    print("Enter 2 for view book:")
    print("Enter 3 for update book:")
    print("Enter 4 for delete book:")
    print("Enter 5 for issue book:")
    print("Enter 6 for return book:")
    print("Enter 7 for exit:")
    choice = int(input("Enter your choice:"))
    if(choice == 1):
        l.add_book()
    elif(choice == 2):
        l.view_book()
    elif(choice == 3):
        l.update_book()
    elif(choice == 4):
        l.delete_book()
    elif(choice == 5):
        l.issue_book()
    elif(choice == 6):
        l.return_book()
    elif(choice == 7):
        break
    else:
        print("Invalid choice")
