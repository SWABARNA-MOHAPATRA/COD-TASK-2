class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

class GradeManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student {name} added.")
        else:
            print(f"Student {name} already exists.")

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].add_grade(grade)
            print(f"Added grade {grade} for {name}.")
        else:
            print(f"Student {name} not found.")

    def view_grades(self, name):
        if name in self.students:
            student = self.students[name]
            print(f"Grades for {name}: {student.grades}")
            print(f"Average grade: {student.average_grade()}")
        else:
            print(f"Student {name} not found.")

    def main_menu(self):
        while True:
            print("\nGrade Manager")
            print("1. Add student")
            print("2. Add grade")
            print("3. View grades")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student name: ")
                self.add_student(name)
            elif choice == '2':
                name = input("Enter student name: ")
                try:
                    grade = float(input("Enter grade: "))
                    self.add_grade(name, grade)
                except ValueError:
                    print("Invalid grade. Please enter a number.")
            elif choice == '3':
                name = input("Enter student name: ")
                self.view_grades(name)
            elif choice == '4':
                print("Exiting the Grade Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = GradeManager()
    manager.main_menu()
