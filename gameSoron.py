import random
potion = 3

def attackEnemy():
    return random.randint(5,10)

def attackSoron():
    return random.randint(5,15)

def usePotion():
    return random.randint(15,50)

life = 50

lifeSoron = 50

print(" ")
print("Bienvenue dans le donjon du Mordor, vous affrontez Soron.")
print(" ")
print("Votre personnage dispose de 3 potions qui vous permette de récupérer des points de vie.")
print(" ")
print("Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.")
print(" ")
while not (life < 0 or lifeSoron < 0):
    print("Point de vie :  "+ str(life))
    print("Point de vie de Sauron :  "+ str(lifeSoron))
    print("Vos potions :  "+ str(potion))
    question = input("Souhaitez-vous attaquer Soron (1) ou utiliser une potion (2)? ")

    if question=="1":
        damageAttack = attackEnemy()
        print(" ")
        print("Soron à subit "+str(damageAttack)+" points de degâts")
        print(" ")
        lifeSoron = lifeSoron - damageAttack
        print("Soron possède "+ str(lifeSoron)+ " points de vie")
        damageSoron = attackSoron()
        life = life - damageSoron
        print(" ")
        print("Soron attaque !  vous perdez "+ str(damageSoron)+ " points de vie")
        print(" ")
        print("Vous possedez "+ str(life)+ " points de vie")
        print(" ")
    elif question=="2":
      if potion > 0:
          potionEffect = usePotion()
          potion = potion - 1
          life = life + potionEffect
          if life > 50 :
              life = 50
          
          print(" Vous avez utilisé une potion ! La potion vous rend "+ str(potionEffect)+ " point de vie")
          print(" ")
          print(" Vous avez  "+ str(life)+ " point de vie")
          life = life - damageSoron
          print(" ")
          print("Soron attaque !  vous perdez "+ str(damageSoron)+ " points de vie")
          print(" ")
          print("Vous possedez "+ str(life)+ " points de vie")
          print(" ")
      else : 
          print(" ")
          print(" Vous ne possedez plus de potion")
    else: 
        input("Instruction non comprise")
if life <= 0:
    print(" SORON A GAGNER  ")
    print(" -------- ")
    print(" GAME OVER ")
elif lifeSoron <= 0:
    print(" Sauron à gagner ! ")
    print(" ")
    print(" Vous avez gagné Sauron félicitation")
