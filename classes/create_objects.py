"""Creation of objects
"""
class DemoClass:
    """A demo class for object creation
    """
    def __init__(self, a, b, c):
        """__init__ can be considered as the instanitiation method of an object

        this double underscore __[some name]__ is the notation for magic
        methods in Python. As you learn deeper, you will get to see __new__,
        __del__, __getattr__ and so on.

        __init__ will initialize an object. so usually here we do necessary
        assignment to attributes for the object just created
        """
        self.a = a
        self.b = b
        self.c = c

    def a_method(self):
        """a normal method just return self's a

        You will notice that this "self"--it is refering to the object itself.
        In Python everything is explicit--so in a method to refer to the object
        you are working on, the first parameter will be the object. Can this
        parameter be named as like "other"?

        Yes you can. But do not try to do it--in dynamic languages we will have
        to follow conventions. self in Python refers to current object by
        convention
        """
        return self.a

    def another_method(self, b):
        """another example of method. with another parameter this time

        Method is just a function. The only difference is that the first
        parameter is the current object for methods. You can have parameters
        of course. However, for methods, normal parameters starts from second
        one.
        """
        # notice that here self.b could be different from b. this is because of
        # namespace--still remember what is namespace right?--a box full of
        # names inside
        print('Inside self, the b is ', self.b)
        print('The parameter b is ', b)
        return self.c + b


a_obj = DemoClass(1, 2, 3)
print('The type of a_obj is ', type(a_obj))
print('The type of a_obj\'s method is ', type(a_obj.a_method))
print('The return value of a_obj.a_method is ', a_obj.a_method())
print('The return value of a_obj.another_method is ', a_obj.another_method(0))

