
"""
this is my class file.
"""



class MyClass:
    """
    My sample class.
    """
    def __init__(self):
        """
        this is my init func.
        """
        self.a = 4
        self.b = 8

    def print_a(self) -> int:
        """
        print self.a attribute and returns it.

        :return: int value
        """
        print(self.a)
        return self.a

    def add_print_b(self, val: int) -> int:
        """
        add input value to self.b and prints it and returns it.

        :param val: value that gets added to self.b
        """
        addition = self.b + val
        print(addition)
        return addition


