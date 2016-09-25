"""Practical examples of classes and objects

Pet is a class: representing the abstraction notion of those lovely animations
that keep us company.
"""
class Pet:
    """A example class to represent pets in real life.

    Of course we will not be able to describe every aspect of pets. Just
    an example.
    """
    healthy_weight_range = (1.5, 4.5)
    favorite_foods = ['meat']

    def __init__(self, name, age, weight, color):
        """Instantiation method for a pet.
        """
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    def have_birthday(self):
        self.age += 1

    def eat_stuff(self, food):
        if food in self.favorite_foods:
            self.weight += 2
        else:
            self.weight += 0.5

    def exercise(self):
        self.weight -= 0.5

    def check_weight(self):
        if self.__is_weight_healthy():
            return False
        else:
            self.send_weight_warning()
            return True

    def speak(self):
        return '{} says love you'.format(self.name)

    def send_weight_warning(self):
        print('Oh, pleas e take note of my weight')

    def __is_weight_healthy(self):
        lower, upper = self.healthy_weight_range
        if lower <= self.weight and self.weight <= upper:
            return True
        else:
            return False

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    print('Let\'s create some pets')
    print('first have a dog')
    dog1 = Pet('a little dog', 1, 1.5, 'Black and white')
    for _ in range(5):
        dog1.eat_stuff('meat')
    while not dog1.check_weight():
        dog1.exercise()
    print(dog1.speak() + '\n')
    print('then a cat')
    cat1 = Pet('a lovely cat', 2, 1.0, 'Black and white')
    cat1.have_birthday()
    print('Now {} is turning into {} years old!'.format(repr(cat1), cat1.age))
    print(cat1.speak())

