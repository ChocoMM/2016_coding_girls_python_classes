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

    def __init__(self, name, age, weight, color, favorite_food, *args, **kwargs):
        """Instantiation method for a pet.

        magic args and kwargs are for later use.
        """
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.favorite_food = favorite_food

    def have_birthday(self):
        self.age += 1

    def eat_stuff(self, food):
        if food == self.favorite_food:
            self.weight += 2
        else:
            self.weight += 0.5

    def exercise(self):
        self.weight -= 0.5

    def check_weight(self):
        if self.__is_weight_healthy():
            pass  # nothing to do
        else:
            self.send_weight_warning()

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

