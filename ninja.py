from pet import Pet
class Ninja:
    def __init__ (self, first_name,last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f'Feeding {self.pet.name} {food}!')
            self.pet.eat()
        else:
            print("Oh no!! you need more pet food")
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise
my_treats = ['Bones', 'Sausage','meat']
my_pet_food = ['Burger', 'grilled']

Lucky = Pet("Lucky", "Dog",["Lucky on things", "is invisible"],"Hey Hey")

Randy = Ninja("Randy","Orton", Lucky, my_treats, my_pet_food)
Randy.feed()
Randy.feed()
Randy.feed()
Randy.walk()