

from src.my_sample_package.my_math_class import MyLib


def test_my_lib_get_hoge():
    obj = MyLib()
    assert obj.get_hoge() == "hoge"