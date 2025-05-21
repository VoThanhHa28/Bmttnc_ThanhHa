from QLSV import QLSV

qlsv = QLSV()
while(True):
    print("\nSTUDENT MANAGEMENT PROGRAM")
    print("*********************MENU************************")
    print("* 1. Add a student")
    print("* 2. Update a student by ID")
    print("* 3. Delete a student by ID")
    print("* 4. Find a student by name")
    print("* 5. Sort list of students by average score")
    print("* 6. Sort list of students by major")
    print("* 7. Show list of students")
    print("* 0. Exit")
    print("*************************************************")
    
    key = int(input("Input your choice: "))
    if (key == 1):
        print("\n1. Add a student")
        qlsv.addStudent()
        print("Add a student successfully")
    elif (key == 2):
        if(qlsv.numberOfStudents() > 0):
            print("2. Update student information")
            print("Input ID: ")
            ID = int(input())
            qlsv.updateStudent(ID)
        else: 
            print("List of students is empty")
    elif (key == 3):
        if(qlsv.numberOfStudents() > 0):
            print("\n3.Delete a student")
            print("Input ID: ")
            ID = int(input())
            qlsv.deleteByID(ID)
        else: 
            print("List of students is empty")
    elif (key == 4):
        if(qlsv.numberOfStudents() > 0):
            print("\n4.Find student by name")
            print("Input name: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showStudent(searchResult)
        else: 
            print("List of students is empty")
    elif (key == 5):
        if(qlsv.numberOfStudents() > 0):
            print("\n5.Sort Student by average score")
            qlsv.sortByAC()
            qlsv.showStudent(qlsv.getListStudent())
        else: 
            print("List of students is empty")
    elif (key == 6):
        if(qlsv.numberOfStudents() > 0):
            print("\n6.Sort list of students by name")
            qlsv.sortByName()
            qlsv.showStudent(qlsv.getListStudent())
        else: 
            print("List of students is empty")
    elif (key == 7):
        if(qlsv.numberOfStudents() > 0):
            print("\n7. Show list of students")
            qlsv.showStudent(qlsv.getListStudent())
        else: 
            print("List of students is empty")
    elif (key == 0):
        print("You  chosen exit the program")
    else: 
        print("Choosing correct function in menu")