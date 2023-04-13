

from src.my_sample_package.my_class import MyClass



def test_my_class_print_a():
    obj = MyClass()
    val = obj.print_a()
    assert val == 4


def test_my_class_add_print_b():
    obj = MyClass()
    val = obj.add_print_b(8)
    assert val == 16


