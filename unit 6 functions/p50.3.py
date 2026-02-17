class Student:
    #using this model creates objects of students 
    def __init__(self, id, name, email, course):
        # Initialize instance variables with the values passed to the constructor
        self.id = id
        self.name = name
        self.email = email
        self.course = course

    def getinfo(self):
        # Print the instance variables
        print(self.id, self.name, self.email, self.course)

# Create an instance of Student with the provided arguments

# topranker1={}
topranker1 = Student(12, 'jay', 'jay@gmail.com', 'bca')
# topranker1={

# "id": 12,
# "name": "jay",
# "email":'jay@gmail.com',
# "course": "bca",

# }
topranker1={}
# Call getinfo to print details
topranker1.getinfo()



# Student={}

# car={}

# name='mercedez'
# car.name=name
# car.model='c-class'
# car.price='2222$'

# {
  
#     'name':'mercedez',
#     'model':'c-class',
#     'price':'2222$',
#     'color':'black',
# }