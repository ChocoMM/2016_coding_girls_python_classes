"""More examples on objects creation
"""
from create_objects import DemoClass

obj1 = DemoClass(1, 2, 'Hello')
print('obj1\'s b is ', obj1.b)
print(
   'Call obj1.another_method for first time: ',
    obj1.another_method(' world!')
)
obj1.c = 'I just said "Hello'
print(
   'Call obj1.another_method after assignment: ',
    obj1.another_method(' world!"')
)

