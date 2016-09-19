"""Demostration of instance methods, class methods and static methods
"""
class MethodsDemoClass:
    """Just to demo use of instance methods, class methods and static methods
    """
    var = 'cls'

    def __init__(self, var):
        self.var = var

    def instance_method(self):
        return self.var

    @classmethod
    def class_method(cls):
        return cls.var

    @staticmethod
    def static_method(var):
        return var


obj = MethodsDemoClass('object')
print('Calling instance method: ', obj.instance_method())
print('Calling class method: ', MethodsDemoClass.class_method())
print('Calling static method: ', MethodsDemoClass.static_method('static'))

