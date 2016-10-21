class Calculator:

    def __init__(self):
        pass

    def sum(self, a, b):
        #Check if a and b are numbers
        #if not numbers throw an exception

        try:
            arg1 = float(a)
        except ValueError:
            return "The given Argument a ist not a number"

        try:
            arg1 = float(b)
        except ValueError:
            return "The given Argument b ist not a number"

        return arg1 + arg2

    def multiply(self, a, b=None):
        if b is None:
            return a*a

        return a*b

    def poweroftwo(self, value):
        return 2 ** value
