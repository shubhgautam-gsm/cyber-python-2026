class Student:
    id = 101
    name = "Pranshu"
    email = "pranshu@abc.com"
    course = "Computer Science"  # Added missing class variable

        
#            classname  key name
print(getattr(Student, 'course'))
# so we get value of above key of Student class

# Attempting to call getinfo() after removing 'course'

