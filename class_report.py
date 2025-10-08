class Report:
    class_std = "9th"
    section = "A"
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
    def show(self):
        print("Student progress report management..>>>")
        print(f"Class:{self.class_std},Section:{self.section}")
        if(self.name and self.rollNo):
            print(f"Student name is:{self.name},rollNo is:{self.rollNo}\n")

class Student(Report):
    def add_student(self):
        self.name = input("Enter student name:")
        self.rollNo = int(input("Enter student rollNo:"))
        with open("class_report.txt","a")as f:
            f.write(f"Class:{self.class_std},Section:{self.section}\n")
            f.write(f"Student name is:{self.name}\n")
            f.write(f"Student rollNo is:{self.rollNo}\n")
        print("Student added successfully")
        self.show()
    
    def add_marks(self):
        marks_dict = {}
        marks_dict["English"] = int(input("Enter english marks:"))
        marks_dict["Hindi"] = int(input("Enter hindi marks:"))
        marks_dict["Math"] = int(input("Enter math marks:"))
        marks_dict["Science"] = int(input("Enter science marks:"))
        marks_dict["History"] = int(input("Enter history marks:"))
        marks_dict["Political"] = int(input("Enter political marks:"))

        total_marks = sum(marks_dict.values())
        max_marks = len(marks_dict)*100
        percentage = (total_marks/max_marks)*100

        with open("class_report.txt","a")as f:
            for subject,marks in marks_dict.items():
                f.write(f"{subject}:{marks}\n")
            f.write(f"Total marks:{total_marks}\n")
            f.write(f"Percentage:{percentage:.2f}%\n")
            f.write("-"*40+"\n")
        
        print("Result Management...>>>")
        for subject,marks in marks_dict.items():
            print(f"{subject}:{marks}")
        print(f"Total marks:{total_marks}") 
        print(f"Percentage:{percentage:.2f}")
        print("Marks added successfully..>>>")

    def view_report(self):
        print("Student Result management..>>>")
        with open("class_report.txt","r")as f:
            lines = f.readlines()
            if(not lines):
                print("Data not found..!!!")
            else:
                for line in lines:
                    print(line.strip())

    def update_student(self):
        print("Student Report management starts updating...>>>")
        roll = int(input("Enter student rollNo:"))
        with open("class_report.txt","r")as f:
            lines = f.readlines()
        update_lines = []
        found = False
        i = 0
        while i <len(lines):
            if(lines[i].startswith("Student rollNo is:")):
                current_roll = int(lines[i].split(":")[1].strip())
                if(current_roll == roll):
                    found = True
                    print("what do you want to update?")
                    print("Enter 1 for update Student name and rollNo")
                    print("Enter 2 for update Student marks")
                    choice = int(input("Enter your choice:"))
                    if(choice == 1):
                        new_name = input("Enter new name:")
                        new_rollNo = input("Enter new rollNo:")
                        update_lines.append(f"Student name is:{new_name}\n")
                        update_lines.append(f"Student rollNo is:{new_rollNo}\n")
                        i+=2 #skip old name and rollNo
                        continue
                    elif(choice == 2):
                        #old name aur rollNo ko copy krlo
                        update_lines.append(lines[i-1])#copy name 
                        update_lines.append(lines[i])#copy rollNo
                        i+=1
                        #now add new marks
                        marks_dict = {}
                        marks_dict["English"] = int(input("Enter new english marks:"))
                        marks_dict["Hindi"] = int(input("Enter new hindi marks:"))
                        marks_dict["Math"] = int(input("Enter new Math marks:"))
                        marks_dict["Science"] = int(input("Enter new science marks:"))
                        marks_dict["History"] = int(input("Enter new history marks:"))
                        marks_dict["Political"] = int(input("Enter new political marks:"))

                        total_marks = sum(marks_dict.values())
                        max_marks = len(marks_dict)*100
                        percentage = (total_marks/max_marks)*100

                        for subject,marks in marks_dict.items():
                            update_lines.append(f"{subject}:{marks}\n")
                        update_lines.append(f"Total marks:{total_marks}\n")
                        update_lines.append(f"Percentage:{percentage:.2f}%\n")
                        update_lines.append("-"*40+"\n")

                        while i< len(lines) and not lines[i].startswith("Class:"):
                            i+=1
                        continue
            update_lines.append(lines[i])
            i+=1
        with open("class_report.txt",'w')as f:
            f.writelines(update_lines)
        if found:
            print("Marks updated successfully..>>>")
        else:
            print("Rollno not found...!!!")

s = Student("","")
while True:
    print("Student report management...>>>")
    print("<<<---Menu--->>>")
    print("Enter 1 for add stduent and marks:")
    print("Enter 2 for view student report:")
    print("Enter 3 for update student or marks:")
    print("Enter 4 for exit:")
    choice = int(input("Enter your choice:"))
    if(choice == 1):
        s.add_student()
        s.add_marks()
        s.show()
    elif(choice == 2):
        s.view_report()
        s.show()
    elif(choice == 3):
        s.update_student()
        s.show()
    elif(choice == 4):
        break
    else:
        print("Invalid choice")
    

