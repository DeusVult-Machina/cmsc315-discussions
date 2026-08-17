"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Animal:
    # Class variable
    kingdom = "Animalia"
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display_info(self):
        print("Name: " + self.name + ", Age: " + self.age)
    pass


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Dog(Animal):
    species = "Canine"

    def __init__(self, name, age, breed, color):
        # Pull variables from animal
        super().__init__(name, age)

        # New variables
        self.breed = breed
        self.color = color
        # New method
    def bark(self):
        print(self.name + "says: Bark!")
    def display_info(self):
        print("Name: " + self.name + ", Age: " + self.age +
        ", Breed: " + self.breed + ", Color: " + self.color)
    pass


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    dog1 = Dog("Disco", 3, "King corso", "Grey")
    dog2 = Dog("Lena", 5, "Pitbull", "Black and white")

    print("Class variable through class:", Dog.species)
    # Access the same class variable through an object
    print("Class variable through dog1:", dog1.species)
    print("Class variable through dog2:", dog2.species)

    dog1.favorite_toy = "Rope"

    # Display each object's namespace
        print("\nDog 1 namespace:")
        print(dog1.__dict__)

        print("\nDog 2 namespace:")
        print(dog2.__dict__)

        # Display the class namespace
        print("\nDog class namespace:")
        print(Dog.__dict__)

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    animal = Animal("Charlie", 4)

    # Add nested mutable data
    animal.favorite_foods = ["Chicken", "Beef", ["Carrots", "Rice"]]

    # Create a shallow copy
    shallow_animal = copy(animal)

    # Create a deep copy
    deep_animal = deepcopy(animal)

    # Modify nested data in the original object
    animal.favorite_foods[2].append("Watermelon")

    print("Original object: ")
    print(animal.__dict__)

    print("\nShallow copy: ")
    print(shallow_animal.__dict__)

    print("\nDeep copy: ")
    print(deep_animal.__dict__)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Class Test ===")
    animal = Animal("Charlie", 4)
    animal.display_info()

    print("\n=== Child Class Test ===")
    dog = Dog("Buddy", 3, "Labrador", "Black")
    dog.display_info()
    dog.bark()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()