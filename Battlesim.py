import random
import time

print ('Welcome')
print ('Loading..')
#Global variables
global mobhp
global charattack
global nmodhp
global chp
#test

#Setting up character
hpUpgrade = 0
charlevel = 0
strUpgrade = 0
exp = 0
charattack = 2 + strUpgrade
chp = 10 + hpUpgrade
charAttackChance = random.randint (1,2)
mobattackchance = random.randint(1,2)
mobhp = chp + random.randint(1,3)
#Setting up monsters
mobattack = chp / 5
#Setting up round
round_complete = False
#Other variables 
s = time.sleep(1)
#Global variables



print ('Loading complete' + '\n')
diff = input('Easy? 1 = yes 2 = no \n')
def roundsp():
     rounds = 1
     print ('Round : %d \n' % rounds)
          #add function for rounds?
def roundsnew():
     if (mobhp <= 0):
          round_complete = True
          round_complete = False
     if(round_complete):
          rounds += 1
def checks(mobhp):
     
     if (mobhp > 0):
          global mobAlive
          mobAlive = True
     return mobhp
def attack():
     if (charAttackChance == 1):
          print('You attacked for %d' % charattack + '\n')
          mobhp - charattack
          time.sleep(1)
     else:
          print('You swing and miss')
     if (mobattackchance == 2):
          print('The Monster attacked for %d' % mobattack + '\n')
          chp - mobattack
          time.sleep(1)
     else:
          print ('The monster swings and misses')
          
     print('Character HP : %d' % chp)
     print('Mob HP : %d' % mobhp)
     
roundsp()
checks(mobhp)
while mobAlive:
     attack() 
