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
        self.shopping == True
        print(f"1) heal:-5 coins, +10 health, \n"
              "2) steroids:-7 coins, +2 attack \n"
              "3) redbull:-10 coins, +2 speed")
        purchase=input("What to Buy? ")
        print(purchase)
        if purchase == ("heal") or ("1"):
            if self.coins>=5:
                self.heal()
                print("Purchased heal \n"
                  f"Your health increased to {self.health}")
            else:
                print("You are too poor\n"
                      f"You have {self.coins} coins")
        elif purchase == ("steroids") or ("2"):
            if self.coins>=7:
                self.steroids()
                print("Purchased steroids \n"
                  f"Your attack increased to {self.attack}")
            else:
                print("You are too poor\n"
                      f"You have {self.coins} coins")
        elif purchase == ("redbull") or ("3"):
            if self.coins>=10:
                self.redbull()
                print("Purchased redbull \n"
                  f"Your speed increased to {self.speed}")
            else:
                print("You are too poor\n"
                      f"You have {self.coins} coins")
        else:
            print("Invalid Item: Retry")
           
p =Player(7, 100, 5, 100, False, False, False)

p.shop()
"""
if p.coins>=15 and p.gun==False:
    p.gun_upgrade()
    p.display()

if p.coins>=30 and p.gun==True and p.grenade==False:
    p.grenade_upgrade()
    p.display()"""

