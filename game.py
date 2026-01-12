
from zombie import Zombie, Regular, Fast, Tank, Boss

import random
class Player:
   def __init__(self, speed, health, attack, coins, gun, grenade,shopping, round_count):
       self.speed = speed 
       self.health = health
       self.attack = attack
       self.coins = coins
       self.gun = gun
       self.grenade = grenade
       self.shopping = shopping
       self.round_count = round_count




   def gun_upgrade(self):
       self.coins-=15
       self.speed+=3
       self.attack+=5
       self.gun=True
       print("Purchased GUN UPGRADE \n"
               f"Your speed increased to {self.speed}\n"
               f"Your attack increased to {self.attack}")
  


   def grenade_upgrade(self):
       self.coins-=30
       self.speed-=3
       self.attack+=5
       self.grenade = True
       print("YOU BOUGHT GRENADE UPGRADE:\n"
                 f"Your attack increased to {self.attack}\n"
                 f"Your speed decreased to {self.speed}")


   def heal(self):
       self.coins-=5
       self.health+=10
       print("Purchased heal \n"
                 f"Your health increased to {self.health}")
   def steroids(self):
       self.coins-=7
       self.attack+=2
       print("Purchased steroids \n"
               f"Your attack increased to {self.attack}")
   def redbull(self):
       self.coins-=10
       self.speed+=2
       print("Purchased redbull \n"
               f"Your speed increased to {self.speed}")


   def regular_kill(self):
       self.coins+=1
   def fast_kill(self):
       self.coins+=3
   def tank_kill(self):
       self.coins+=5
   def boss_kill(self):
       self.coins+=12
      
   def display(self):
      print(f'Round: {self.round_count}')
      print(f'Coin(s): {self.coins}')
      print(f'Speed: {self.speed}')
      print(f'Health: {self.health}')
      print(f'Attack: {self.attack}')
      if self.gun ==True:
          print("GUN UPGRADE")
      if self.grenade ==True:
          print("GRENADE UPGRADE")
      if self.health <=0:
          print("You LOST")
   def broke(self):
       print("You are too poor\n"
               f"You have {self.coins} coins")
      
   def shop(self):
       self.shopping = True
       while self.shopping == True:
           print(f"1) Healing Potion:-5 coins, +10 health, \n"
             "2) Steroids:-7 coins, +2 attack \n"
             "3) Redbull:-10 coins, +2 speed\n"
             "ONE TIME PURCHASES:\n"
             "4) GUN UPGRADE: -15 coins, +3 speed, +5 attack\n"
             "5) GRENADE UPGRADE: -30 coins, -3 speed, +5 attack\n")
           "0)EXIT\n"
           purchase=input("What to Buy? ").lower().strip()
           print(purchase)
           if purchase in ("heal","1"):
               if self.coins>=5:
                   self.heal()
                   self.shopping = False
                   break
               else:
                   self.broke()
           elif purchase in ("steroids","2"):
               if self.coins>=7:
                   self.steroids()
                   self.shopping = False
                   break
               else:
                   self.broke()
           elif purchase in ("redbull", "3") :
               if self.coins>=10:
                   self.redbull()
                   self.shopping = False
                   break
               else:
                   self.broke()
           elif purchase in("gun", "4", "gun upgrade"):
               if self.gun==False:
                   if self.coins>=15:
                       self.gun_upgrade()
                       self.shopping = False
                       break
                   else:
                       self.broke()
               else:
                   print("Already Purchased GUN UPGRADE")
           elif purchase in("grenade", "5", "grenade upgrade"):
               if self.grenade==False:
                   if self.coins>=30:
                       self.grenade_upgrade()
                       self.shopping = False
                       break
                   else:
                       self.broke()
               else:
                   print("Already Purchased GRENADE UPGRADE")
           elif purchase in("exit", "0"):
               self.shopping = False
               print("Left Shop")
               break
           else:
               print("Invalid Item: Retry")
      
   def round (self):
       self.round_count+=1
  
   def spawning(self):
       random_number = random.randint(1,6)
       if self.round_count == 11:
           return Boss()
       if random_number <= 3:
           return Regular()
       elif random_number in (4,5):
           return Fast()
       else:
           return Tank()


         
p =Player(7, 100, 5, 50, False, False, False,0)


while p.round_count<12 and p.health>0:
   #z = Zombie(0,0,0,"Place Holder")
   z=p.spawning()




   while p.health >0 and z.health>0:


       if z.speed <= p.speed:
           z.health = z.health - p.attack
           print(f"\nYou attacked the zombie! The zombie's health is {z.health} now")
           if z.health <= 0:
               break
           p.health = p.health - z.attack 
           print(f"The zombie attacked you! Your health is {p.health} now")
           if p.health <= 0:
               break




       elif z.speed > p.speed:
           p.health = p.health - z.attack
           print(f"\nThe zombie attacked you! Your health is {p.health} now")
           if p.health <= 0:
               break
           z.health = z.health - p.attack
           print(f"You attacked the zombie! The zombie's health is {z.health} now")
           if z.health <= 0:
               break


   if z.health <= 0:
       print(f"You defeated {z.title}")
       if z.title == "regular":
           p.regular_kill()
       if z.title == "fast":
           p.fast_kill()
       if z.title == "tank":
           p.tank_kill()
       if z.title == "boss":
           p.boss_kill()


       p.round()
       print(f"Coins: {p.coins}\n"
               f"Round: {p.round_count}")
       p.display()
       p.shop()


   if p.health <= 0:
       print(f"You Lose! You only survived to round {p.round_count}\n"
             f"Defeated by {z.title}")
       p.display()




