class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        self.recommended_food = 'kibble'

    def describe_dog(self):
        """Gives basic description of the dog's attributes"""
        print(self.name.title() + " is " + str(self.age) + " years old.")

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

    def read_recommended_food(self):
        """Print a statement saying the recommended food"""
        print("You should feed the dog " + self.recommended_food + ".")

    def update_age(self, age):
        """Updates the age of the dog to user input"""
        self.age = age

    def birthday(self):
        """Updates the age of the dog to user input"""
        self.age += 1


my_dog = Dog('lucy', 4)
my_dog.update_age(5)
my_dog.birthday()
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
my_dog.read_recommended_food()


class Double_Doodle(Dog):
    """Represent a specific breed of dog: double doodle"""

    def __init__(self, name, age):
        """Initialize the attributes of the parent class"""
        super().__init__(name, age)


my_doodle = Double_Doodle('lucy', 5)
my_doodle.describe_dog()
my_doodle.read_recommended_food()
