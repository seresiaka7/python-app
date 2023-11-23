
#Apprendre python
#Operators et variables 
name="sere "
last100="siaka"
print(name+"     "+last100)

# Typage en python
first="sere"
two= 33.4433
three=True
intboo=bool(22)
five=[2,4]
six=(3,2)
seven={"nom":"jean"}

print(f"le type est 1 : {type(first)}")
print(f"le type est 2: {type(two)}")
print(f"le type est 3: {type(three)}")
print(f"le type est 4: {type(intboo)}")
print(f"le type est  5: {type(five)}")
print(f"le type est 6: {type(six)}")
print(f"le type est  7: {type(seven)}")



#Boucles en python len(name)
i=1
for i in range(3):
    if name[1]=='e':
       print("hello world"+" "+name[1])
    elif  name[1] != 'e':
        print("Welcome")
    print("Bienvenue dans la programmation") 

j=1
while j<=2:
    print(f"Felicitation :${last100[-3:5]}")
    j=j+1

# f-string  avec le jeu de la devinette 
import random
a=1
dev=random.randint(1,100)
while a<=10:

    mot=int(input("Saisir le nombre :"))
    
   
    if mot<dev:
         print(f"Le nombre est  plus grand  : {dev}")
         print(f"Vous êtes à votre {a} essais ")
    elif mot>dev:
         print(f"Le nombre est  plus petit  : {dev}")
         print(f"Vous êtes à votre {a} essais  ")
    else :
        print(f"Félicition vous avez gagné à {a} essais: {dev}")
        break
       
       
     
    a=a+1


#Compter le nombre d'occurence de 4

nb="214422377"
s=0
for k in range(len((nb))):
    if int(nb[k])==7:
        s+=1
        
    
print(f"Bravo le nombre de la lettre  2 est : {s}")