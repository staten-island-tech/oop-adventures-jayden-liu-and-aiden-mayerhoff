class Zombie:
    def __init__(self, speed, health, attack, title):
        self.speed = speed
        self.health = health
        self.attack = attack
        self.title =title


    def display(self):
        print(f'title: {self.title}')
        print(f'speed: {self.speed}')
        print (f'health: {self.health}')
        print(f'attack: {self.attack}') 

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
        print("Here comes the BOSS")
