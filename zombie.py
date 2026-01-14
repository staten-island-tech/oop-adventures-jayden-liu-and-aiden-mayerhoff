from game import Player
class Zombie:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, speed, health, attack, round_count):
        self.speed = speed
        self.health = health
        self.attack = attack
        self.round_count =round_count
=======
    def __init__(self, speed, health, attack, title):
        self.speed = speed
        self.health = health
        self.attack = attack
        self.title =title
>>>>>>> 65f40b1ac1744d32906f219866562fa8034a89fb
=======
    def __init__(self, speed, health, attack, title):
        self.speed = speed
        self.health = health
        self.attack = attack
        self.title =title
>>>>>>> 65f40b1ac1744d32906f219866562fa8034a89fb
=======
    def __init__(self, speed, health, attack, title):
        self.speed = speed
        self.health = health
        self.attack = attack
        self.title =title
>>>>>>> 65f40b1ac1744d32906f219866562fa8034a89fb
=======
    def __init__(self, speed, health, attack, title):
        self.speed = speed
        self.health = health
        self.attack = attack
        self.title =title
>>>>>>> 906d8d7ead8e028797d6f6a931ebe4f9b5ff91d5


    def display(self):
        print(f'title: {self.title}')
        print(f'speed: {self.speed}')
        print (f'health: {self.health}')
        print(f'attack: {self.attack}') 
    def random(self):
        import random
        random_number = random.randint(1,6)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if random_number <= 3: 
            self.regular()
            self.display()
            print("You've encountered a Regular zombie!")

        if random_number == 4 or random_number == 5:
            self.fast()
            self.display()
            print("You've encountered a Fast zombie!")
    
        if random_number == 6:
            self.tank()
            self.display()
            print("You've encountered a Tank zombie!")
    def round (self):
        self.round_count=-1
                

<<<<<<< HEAD
z = Zombie(0,0,0)
p =Player(7, 100, 5, 100, False, False, False, 10)

#p.shop()
z.random()

while z.round_count>=1:
    while z.speed < p.speed:
        z.health = z.health - p.attack 
        print("You attacked the zombie! The zombie's health is {z.health} now")
        p.health = p.health - z.attack
        print("The zombie attacked you! Your health is {z.health} now")

    while p.speed < z.speed:
        p.health = p.health - z.attack
        print("The zombie attacked you! Your health is {z.health} now")
        z.health = z.health - p.attack 
        print("You attacked the zombie! The zombie's health is {z.health} now")
    z.round()
=======
=======
>>>>>>> 65f40b1ac1744d32906f219866562fa8034a89fb
=======
>>>>>>> 65f40b1ac1744d32906f219866562fa8034a89fb
=======
>>>>>>> 906d8d7ead8e028797d6f6a931ebe4f9b5ff91d5
class Regular(Zombie):
    def __init__(self):
        super().__init__(speed=5, health=10, attack=5, title ="regular")
        self.display()
        print("You've encountered a Regular zombie!")
class Fast(Zombie):
    def __init__(self):
        super().__init__(speed=10, health=7, attack=8, title ="fast")
        self.display()
        print("You've encountered a Fast zombie!")
class Tank(Zombie):
    def __init__(self):
        super().__init__(speed=4, health=25, attack=10, title ="tank")
        self.display()
        print("You've encountered a Tank zombie!")
class Boss(Zombie):
    def __init__(self):
        super().__init__(speed=7, health=50, attack=15, title ="boss")
        self.display()
<<<<<<< HEAD
        print("Here comes the BOSS")
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65f40b1ac1744d32906f219866562fa8034a89fb
=======
>>>>>>> 65f40b1ac1744d32906f219866562fa8034a89fb
=======
>>>>>>> 65f40b1ac1744d32906f219866562fa8034a89fb
=======
        print("YOU ARE FINALLY FACING THE BOSS!!!")
>>>>>>> 906d8d7ead8e028797d6f6a931ebe4f9b5ff91d5
