import os


class Course:
    def __init__(self, course_id, name, capacity):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []  # List of student IDs

    def get_seats_left(self):
        return self.capacity - len(self.enrolled_students)


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.registered_courses = []  # List of course IDs


class RegistrationSystem:
    def __init__(self, filename="registrations.txt"):
        self.filename = filename
        self.courses = {
            "CS101": Course("CS101", "Programming", 2),
            "MA101": Course("MA101", "Mathematics", 30),
            "PH101": Course("PH101", "Physics", 30),
        }
        self.students = {}
        self.clear_file()  # Ensure we start from an empty registrations.txt for test cases

    def clear_file(self):
        """Initializes/clears the database file."""
        with open(self.filename, "w") as f:
            f.write("")

    def save_to_file(self):
        """Saves current state to registrations.txt."""
        with open(self.filename, "w") as f:
            for student in self.students.values():
                courses_str = ",".join(student.registered_courses)
                f.write(f"{student.student_id}|{student.name}|{courses_str}\n")

    def register_course(self, student_id, name, course_id):
        # 1. Validate course existence
        if course_id not in self.courses:
            print(f"Course {course_id} does not exist.")
            return

        course = self.courses[course_id]

        # 2. Fetch or create student record
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)

        student = self.students[student_id]

        # 3. Validate duplicate and max enrollment rules
        if course_id in student.registered_courses:
            print(f"{student.name} ({student_id}) is already enrolled in {course_id}.")
            return

        if len(student.registered_courses) >= 3:
            print(f"Registration rejected. Student cannot enroll in more than 3 courses.")
            return

        if course.get_seats_left() <= 0:
            print(f"Course {course_id} is full.")
            return

        student.registered_courses.append(course_id)
        course.enrolled_students.append(student_id)
        self.save_to_file()
        print(f"{student.name} ({student_id}) registered for {course_id}. Seats left: {course.get_seats_left()}")

    def drop_course(self, student_id, course_id):
        if student_id not in self.students:
            print(f"Student {student_id} not found.")
            return

        if course_id not in self.courses:
            print(f"Course {course_id} does not exist.")
            return

        student = self.students[student_id]
        course = self.courses[course_id]

        if course_id not in student.registered_courses:
            print(f"{student.name} ({student_id}) is not enrolled in {course_id}.")
            return

        student.registered_courses.remove(course_id)
        course.enrolled_students.remove(student_id)
        self.save_to_file()
        print(f"{student.name} ({student_id}) dropped {course_id}. Seats left: {course.get_seats_left()}")

    def view_student(self, student_id):
        if student_id not in self.students:
            print(f"Student {student_id} not found.")
            return

        student = self.students[student_id]
        if not student.registered_courses:
            print(f"{student.name} ({student_id}) has no registered courses.")
            return

        print(f"\n---Registration Profile for {student.name} ({student_id}) ---")
        for course_id in student.registered_courses:
            course = self.courses[course_id]
            print(f"- {course.course_id}: {course.name}")

    def view_course_list(self):
        print("\n--- Current Course Status ---")
        for course_id, course in self.courses.items():
            print(f"{course_id} - {course.name} | capacity: {course.capacity} | Seats Available: {course.get_seats_left()}")


def main():
    system = RegistrationSystem()

    while True:
        print("\n=========================================")
        print("   STUDENT COURSE REGISTRATION SYSTEM  ")
        print("=========================================")
        print("1. Register Course")
        print("2. Drop Course")
        print("3. View Student Profile")
        print("4. View All Courses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            s_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            c_id = input("Enter Course ID: ").strip().upper()
            system.register_course(s_id, name, c_id)

        elif choice == "2":
            s_id = input("Enter Student ID: ").strip()
            c_id = input("Enter Course ID to drop: ").strip().upper()
            system.drop_course(s_id, c_id)

        elif choice == "3":
            s_id = input("Enter Student ID: ").strip()
            system.view_student(s_id)

        elif choice == "4":
            system.view_course_list()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()