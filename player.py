class Player:
    def __init__(self, speed, health, attack, coins, gun, grenade,shopping):
        self.speed = speed  
        self.health = health
        self.attack = attack 
        self.coins = coins
        self.gun = gun
        self.grenade = grenade
        self.shopping =shopping


    def gun_upgrade(self):
        self.coins-=15
        self.speed+=3
        self.attack+=5
        self.gun=True
        print("YOU BOUGHT GUN UPGRADE:") 
    
    def grenade_upgrade(self):
        self.coins-=30
        self.speed-=3
        self.attack+=5
        self.grenade = True
        print("YOU BOUGHT GRENADE UPGRADE:")

    def heal(self):
        self.coins+-5
        self.health+=10
    def steroids(self):
        self.coins+-7
        self.attack+=2
    def redbull(self):
        self.coins+-10
        self.speed+=2

    def regular_kill(self):
        self.coins+=1
    def speed_kill(self):
        self.coins+=3
    def tank_kill(self):
        self.coins+=5
    def boss_kill(self):
        self.coins+=12
        
    def display(self):
       print(f'Speed: {self.speed}')
       print(f'Health: {self.health}')
       print(f'Attack: {self.attack}')
       if self.gun ==True:
           print("GUN UPGRADE")
       if self.grenade ==True:
           print("GRENADE UPGRADE")
    
    def shop(self):
        self.shopping == False
        print(f"heal:-5c, +10h, \n"
              "steroids:-7c, +2a \n"
              "redbull:-10c, +2s")
        purchase=input("What to Buy? ")
        while self.shopping ==True:
            for i in ["heal, steroids, redbull"]:
                if purchase != i:
                    print("Try again")
                    break
           
p =Player(7, 100, 5, 0, False, False, False)

p.shop()
if p.coins>=15 and p.gun==False:
    p.gun_upgrade()
    p.display()

if p.coins>=30 and p.gun==True and p.grenade==False:
    p.grenade_upgrade()
    p.display()

