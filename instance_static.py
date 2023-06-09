# 2. Define a static variable and access that through a instance
class MyClass:
    static_var = 0

    def __init__(self):
        MyClass.static_var += 1
        self.instance_var = MyClass.static_var


