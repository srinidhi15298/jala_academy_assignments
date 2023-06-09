""" Define the local and Global variables with the same name and print both variables and
understand the scope of the variable """

a = 10


def func():
    a = 5
    print("a will become local variable here and its value = ", a)


func()
print("a will turn as global variable here and its value = ", a)

