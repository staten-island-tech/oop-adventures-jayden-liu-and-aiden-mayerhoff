from game import Player
class Zombie:
    def __init__(self, speed, health, attack, round_count):
        self.speed = speed
        self.health = health
        self.attack = attack
        self.round_count =round_count

    def regular (self):
        self.speed = 5
        self.health = 10
        self.attack = 5

    def fast (self):
        self.speed=10
        self.health=7
        self.attack = 8

    def tank(self):
        self.speed = 5
        self.health = 25
        self.attack = 10

    def boss(self):
        self.speed = 10
        self.health = 50
        self.attack = 15

    def display(self):
        print(f'speed: {self.speed}')
        print (f'heath: {self.health}')
        print(f'attack: {self.attack}') 
    def random(self):
        import random
        random_number = random.randint(1,6)

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