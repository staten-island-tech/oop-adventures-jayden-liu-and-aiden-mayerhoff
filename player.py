class Player:
    def __init__(self, speed, health, attack, coins):
        self.speed = speed  
        self.health = health
        self.attack = attack

    def gun_upgrade(self):
        coins-=15
        self.speed+=3
        self.attack+=5
        print("Your auto bought GUN UPGRADE")
    
    def grenade_upgrade(self):
        coins-=30
        self.speed-=3
        self.attack+=5

    def regular_kill(self):
        coins+=1
    def speed_kill(self):
        coins+=3
    def tank_kill(self):
        coins+=8
    def boss_kill(self):
        coins+=25
        
    def display(self):
       print(f'Speed: {self.speed}')
       print(f'Health: {self.health}')
       print(f'Attack: {self.attack}')
p =Player(7, 100, 5)

if p.coins>=15:
    p.gun_upgrade()

