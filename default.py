# Python Program to Calculate Total Marks Percentage and Grade of a Student Using Class

class StudentGradeTracker:
    def __init__(self):
        self.students = {}

    def display_menu(self):
        print("=" * 50)
        print("Please select an option from the following menu")
        print("=" * 50)
        print("1. Enter grade of a student")
        print("2. Display list of students")
        print("3. Calculate average grade of the class")
        print("4. Display name of student with the highest grade")
        print("5. Display name of student with the lowest grade")
        print("6. Quit")

    def enter_grade(self):
        student_id = input("Enter the student's ID: ")
        student_name = input("Enter the student's name: ")
        final_grade = input("Enter the student's grade: ")

        self.students[student_id] = [student_name, final_grade]

    def display_students(self):
        print("The students in our list are:")
        for student_id, info in self.students.items():
            print(f"{student_id} : {info}")

    def calculate_average_grade(self):
        if not self.students:
            print("No students in the list.")
            return

        total_grades = sum(int(info[1]) for info in self.students.values())
        average_grade = total_grades / len(self.students)
        print(f"The average grade of all the students is: {average_grade:.2f}")

    def display_highest_grade_student(self):
        if not self.students:
            print("No students in the list.")
            return

        highest_grade_student = max(self.students, key=lambda k: int(self.students[k][1]))
        print(f"The student with the highest grade is: {self.students[highest_grade_student][0]}")

    def display_lowest_grade_student(self):
        if not self.students:
            print("No students in the list.")
            return
        def run_program(self):
while True:
  self.display_menu()
  option = input("Enter an option from the menu (1, 2, 3, 4, 5, or 6): ")
if option == '1':
                self.enter_grade()
elif option == '2':
                self.display_students()
elif option == '3':
                self.calculate_average_grade()
elif option == '4':
                self.display_highest_grade_student()
elif option == '5':
                self.display_lowest_grade_student()
elif option == '6':
 print(">> Exiting the program.")
break
else:
print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    tracker = StudentGradeTracker()
    tracker.run_program()
