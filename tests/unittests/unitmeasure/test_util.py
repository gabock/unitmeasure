import pytest

from unitmeasure.util import classproperty


def test_classproperty_get():

    class A(object):

        @classproperty
        def a(cls):
            return 5

    a = A()
    assert a.a == 5


def test_classproperty_set():

    class A(object):

        @classproperty
        def a(cls):
            return 5

    a = A()
    with pytest.raises(AttributeError):
        a.a = 10
