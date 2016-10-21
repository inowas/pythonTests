def run_once(f):
    """
    >>> @run_once
    ... def f(n): return 2 + 3

    >>> f(5)
    5
    """
    def _f(*args, **kwargs):
        if not hasattr(_f, "_retval"):
            _f._retval = f(*args, **kwargs)
        return _f._retval
    return _f
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()