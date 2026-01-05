class Player:
    def __init__(self, speed, health, attack, coins, gun, grenade):
        self.speed = speed  
        self.health = health
        self.attack = attack 
        self.coins = coins
        self.gun = gun
        self.grenade = grenade


    def gun_upgrade(self):
        self.coins-=15
        self.speed+=3
        self.attack+=5
        self.gun=True
        print("YOU AUTO-BOUGHT GUN UPGRADE:") 
    
    def grenade_upgrade(self):
        self.coins-=30
        self.speed-=3
        self.attack+=5
        self.grenade = True
        print("YOU AUTO-BOUGHT GRENADE UPGRADE:")

    def regular_kill(self):
        self.coins+=1
    def speed_kill(self):
        self.coins+=3
    def tank_kill(self):
        self.coins+=8
    def boss_kill(self):
        self.coins+=25
        
    def display(self):
       print(f'Speed: {self.speed}')
       print(f'Health: {self.health}')
       print(f'Attack: {self.attack}')
       if self.gun ==True:
           print("GUN UPGRADE")
       if self.grenade ==True:
           print("GRENADE UPGRADE")
           
p =Player(7, 100, 5, 45, False, False)

if p.coins>=15:
    p.gun_upgrade()
    p.display()

if p.coins>=30 and p.gun==True:
    p.grenade_upgrade()
    p.display()

