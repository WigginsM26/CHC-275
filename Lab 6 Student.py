"""
Name:
Section:
Description: Template for Lab 5
"""

"""
Scenario: we live in a world where blackbaud no longer exists. our job is to write
a student records program that can print out the transcript, grade level, and email of our students.
You are to implement this using functions, dictionaries, and lists
"""


def getStudent(directory, student):
    if student in directory:
        return directory[student]["grades"], directory[student]["grade_level"], directory[student]["email"]
    else:
        return None 


def getStudentGrades(directory, student):
    if student in directory:
        return directory[student]["grades"]
    return None


def getStudentGradeLevel(directory, student):
    if student in directory:
        return directory[student]["grade_level"]
    return None


def getStudentEmail(directory, student):
    if student in directory:
        return directory[student]["email"]
    return None


def getGradeLevel(directory, gradelevel):
    for student in directory:
        if directory[student]["grade_level"] == gradelevel:
            print(student)


def addStudent(directory):
    name = input("Enter student name: ")
    grade_level = int(input("Enter grade level: "))
    email = input("Enter email: ")

    grades = {}
    num_classes = int(input("How many classes? "))

    for i in range(num_classes):
        course = input("Enter course name: ")
        grade = int(input("Enter grade: "))
        grades[course] = grade

    directory[name] = {
        "grades": grades,
        "grade_level": grade_level,
        "email": email
    }


def removeStudent(directory, student):
    if student in directory:
        del directory[student]
        print("Student removed.")
    else:
        print("Student not found.")


def updateGrade(directory, student):
    if student in directory:
        course = input("Enter course to update: ")
        if course in directory[student]["grades"]:
            new_grade = int(input("Enter new grade: "))
            directory[student]["grades"][course] = new_grade
        else:
            print("Course not found.")
    else:
        print("Student not found.")


def calculateGPA(directory, student):
    if student in directory:
        grades = directory[student]["grades"].values() # looked up, forgot abt the .values() method
        if len(grades) == 0:
            return 0
        return sum(grades) / len(grades)
    return 0


def checkHonorRoll(directory, student):
    if student in directory:
        grades = directory[student]["grades"].values()
        gpa = calculateGPA(directory, student)

        for grade in grades:
            if grade < 81:
                return False

        if gpa >= 88:
            return True
    return False


def printMenu():
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Student Info")
    print("4. View Students by Grade Level")
    print("5. Update Grade")
    print("6. Calculate GPA")
    print("7. Check Honor Roll")
    print("8. Quit")


def main():
    Students = {}

    while True:
        printMenu()
        choice = input("Enter choice: ")

        if choice == "1":
            addStudent(Students)

        elif choice == "2":
            name = input("Enter student name: ")
            removeStudent(Students, name)

        elif choice == "3":
            name = input("Enter student name: ")
            data = getStudent(Students, name)
            if data:
                grades, level, email = data
                print("Grades:", grades)
                print("Grade Level:", level)
                print("Email:", email)
            else:
                print("Student not found.")

        elif choice == "4":
            level = int(input("Enter grade level: "))
            getGradeLevel(Students, level)

        elif choice == "5":
            name = input("Enter student name: ")
            updateGrade(Students, name)

        elif choice == "6":
            name = input("Enter student name: ")
            print("GPA:", calculateGPA(Students, name))

        elif choice == "7":
            name = input("Enter student name: ")
            if checkHonorRoll(Students, name):
                print("Honor Roll: Made honor roll")
            else:
                print("Honor Roll: Did not make honor roll.")

        elif choice == "8":
            print("Ending program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()