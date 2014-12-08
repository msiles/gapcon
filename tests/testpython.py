__author__ = 'moisessiles'


class TestPython:

    def test_foo(a, b):
        print "value for A: [{}] and value for B [{}]".format(a, b)

    a_tuple = ("Tuple A", "Tuple B")
    arr = ("Arr A", "Arr B")

    test_foo(arr[0], arr[1])
    test_foo(*a_tuple)

    test_foo(*arr)
    test_foo(a_tuple[0], a_tuple[1])