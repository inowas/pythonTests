# coding: utf-8

def run_once(f):
    """
    Мемоизация. Не зависит от аргументов.
    """
    def _f(*args, **kwargs):
        if not hasattr(_f, "_retval"):
            _f._retval = f(*args, **kwargs)
        return _f._retval
    return _f


def test_run_once():
    @run_once
    def sum(self, a, b):
        return a + b

    # это результат вызова функции inc()...
    assert (2 + 3) == 5

