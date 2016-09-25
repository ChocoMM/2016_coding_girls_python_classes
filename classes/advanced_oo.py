"""Demostration of different notions in advanced object oriented programming
"""
from practical_class_object import Pet


class Dog(Pet):
    favorite_foods = ['meat', 'bone']
    
    def speak(self):
        return 'woof-woof, {} says love you'.format(self.name)


class Cat(Pet):
    favorite_foods = ['meat', 'fish']

    def speak(self):
        return 'meow-meow, {} says love you'.format(self.name)


class DangerousPet:
    def speak(self):
        return 'I am just dangerous'

    def is_angry(self):
        print('Warning!!! Be careful and try not to further piss it off')


class Cheetah(DangerousPet, Pet):
    healthy_weight_range = (25, 45)


if __name__ == '__main__':
    print('Let\'s create some pets')
    print('first have a dog')
    dog1 = Dog('a little dog', 1, 1.5, 'Black and white')
    for _ in range(5):
        dog1.eat_stuff('bone')
    while not dog1.check_weight():
        dog1.exercise()
    print(dog1.speak() + '\n')
    print('then a cat')
    cat1 = Cat('a lovely cat', 2, 1.0, 'Black and white')
    cat1.have_birthday()
    for _ in range(5):
        cat1.eat_stuff('bone')
    print('Now {} is turning into {} years old!'.format(repr(cat1), cat1.age))
    print(cat1.speak() + '\n')
    print('and a cheetah')
    the_cheetah = Cheetah('Handsome and dangerous cheetah', 5, 30, 'yellow and black')
    print(the_cheetah.speak())
    the_cheetah.is_angry()

