class Student_Report:
    class_std = "9th"
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
    def show(self):
        print(f"{self.name}")
        print(f"{self.rollNo}")
class Student_Marks(Student_Report):
    def __init__(self,name="",rollNo=""):
        super().__init__(name,rollNo)
    def add_Student(self):
        name = input("Enter Name:")
        rollNo = input("Enter RollNo:")    
        with open("Student_result.txt","a")as f:
            f.write(f"{name}|{rollNo}|\n")
            print("Name|RollNo|")
        Student = Student_Report(name,rollNo)
        Student.show()
    
    def subject_marks(self):
        marks_dict ={}
        marks_dict["English"] = int(input("Enter English marks:"))
        marks_dict["Hindi"] = int(input("Enter Hindi marks:"))
        marks_dict["Math"] = int(input("Enter Math marks:"))
        marks_dict["Science"] = int(input("Enter Science marks:"))
        marks_dict["Political"] = int(input("Enter Political marks:"))
        marks_dict["History"] = int(input("Enter History marks:"))

        total_marks = sum(marks_dict.values())
        percentage = total_marks/(len(marks_dict)*100)*100

        with open("Student_result.txt","a")as f:
            for subject,marks in marks_dict.items(): 
                f.write(f"{subject}:{marks}|")

            f.write(f"Total:{total_marks} Percentage:{percentage:.2f}%\n")
            
            print("Result...>>>")
            for subject,marks in marks_dict.items():
                print(f"{self}")
                print(f"{subject}:{marks}")
            print(f"Total marks:{total_marks}")
            print(f"Percentage:{percentage:.2f}%")
    
    def view_Result(self):
        print("Student record management...!!!")
        with open("Student_result.txt","r")as f:
            lines = f.readlines()
            if(not lines):
                print("file not found")
            else:
                for line in lines:
                    data = line.strip().split("|")
                    print("|".join(data))

Student = Student_Marks()

while True:
    print("Enter 1 for add student")
    print("Enter 2 for add student marks ")
    print("Enter 3 for to view student_Report")
    print("Enter 4 to end")
    choice = int(input("Enter your choice:"))
    if(choice == 1):
        Student.add_Student()
    elif(choice == 2):
        Student.subject_marks()
    elif(choice == 3):
        Student.view_Result()
    elif(choice == 4):
        print("End")
        break
    else:
        print("invalid Report")

                              
                    

            



        