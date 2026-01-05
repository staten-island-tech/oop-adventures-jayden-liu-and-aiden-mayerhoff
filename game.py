class Zombie:
    def __init__(self, speed, health, attack):
        self.speed = speed
        self.health = health
        self.attack = attack

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

z = Zombie(0,0,0)
z.boss()
z.display()
         
