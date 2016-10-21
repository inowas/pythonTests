class Calculator:

    def __init__(self):
        pass

    def sum(self, a, b):
        return a+b

    def multiply(self, a, b=None):
        if b is None:
            return a*a

        return a*b

    def poweroftwo(self, value):
        return 2 ** value
