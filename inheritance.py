class A(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False

    def display(self):
        print("Inside A")


class B(A):

    # Here we return true
    def isEmployee(self):
        return True

    def display(self):
        print("Inside B")

class C(B):

    # Here we return true
    def display(self):
        print("Inside C")
    def isEmployee(self):
        return True

# Driver code
if __name__ == '__main__':

    emp = A("Geek1")  # An Object of A
    print(emp.getName())

    emp1 = B("Geek2")  # An Object of B
    print(emp1.getName(),emp1.display())

# Driver code
    emp2 = C("Geek3")  # An Object of A
    print(emp2.getName(), emp2.display())

