class Employee:
    # Parameterized Constructor

    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d Name: %s"%(self.id, self.name))
        # print("ID:", self.id,"Name:", self.name)


# Creating instances and calling methods
emp1 = Employee( 101,"John")
emp2 = Employee("David", 102)
emp1.display()
emp2.display()
