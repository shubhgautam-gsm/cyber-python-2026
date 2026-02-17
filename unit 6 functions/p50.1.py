class Student:
    id = 101
    name = "Pranshu"
    email = "pranshu@abc.com"
    course = "Computer Science"  # Added missing class variable

    def getinfo(self):
        print(self.id, self.name, self.email, self.course)

# Create an instance of Student
student_instance = Student()

# Call getinfo to print details
student_instance.getinfo()

# Access the id attribute directly
print(student_instance.id)  # This will print 101
