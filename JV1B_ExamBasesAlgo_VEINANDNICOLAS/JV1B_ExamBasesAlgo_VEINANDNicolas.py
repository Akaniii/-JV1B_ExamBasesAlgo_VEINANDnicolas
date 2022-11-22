
#Partie 1 tri a bulles a)
myTable=[2,36,40,28,8,12]
stock=0
stock=myTable[2]
myTable[2]=myTable[5]
myTable[5]=stock
print(myTable)

#b) 
for i in range (len(myTable)):
    if(myTable[i]>myTable[i+1]):
      stock=myTable[i]
      myTable[i]=myTable[i+1]
      myTable[i+1]=stock
    print(myTable)

#c) il n'est pas réussi, je n'ai pas trouvé comment relancer le programme pour qu'il reparte au début du tableau


for i in range (len(myTable)):
    if(myTable[i]>myTable[i+1]):
        stock=myTable[i]
        myTable[i]=myTable[i+1]
        myTable[i+1]=stock
    else: i=0    
    print(myTable)
           
#4) Le tri a bulle est très lent car plus de donné seront présentes dans un tableau et plus l'algorithmes sera long, c'est à dire que le besoin en énergie/temps est exponentielle en fonction du nombre de données, car pour le tri a bulle le programme a besoin de retourne au début du tableau une fois qu'il a rangé la donné la plus élevé.
 
 #PARTIE 2
 # 1)
ligne1='|-|-|-|'           
ligne2='|-|-|-|' 
ligne3='|-|-|-|'     
print(ligne1)
print(ligne2)
print(ligne3)
tab1=[0,0,0]
tab2=[0,0,0]
tab3=[0,0,0]
#b) 
joueur1='X'
joueur2='O'

print('vous voulez jouer les O ou les X?')
choixpion=input()
if(choixpion=='O'):
    joueur=joueur2

if(choixpion=='X'):
    joueur=joueur1    


print('voici les explications de jeu, pour jouer il faut écrire dans la console les bonnes coordonées, si vous voulez jouer en haut a gauche il faut taper a1. ' )
print('en clair les lignes sont indiqué par les lettres a, b et c et les colonnes par les chiffres de 1à3')

print('cest a vous de jouer, veuillez rentrer les coordonnées de jeu')
choixjoueur=input()

if (choixjoueur=="a1"):
    tab1[0]=1  
if (choixjoueur=="a2"):
    tab1[1]=1
if (choixjoueur=="a3"):
     tab1[2]=1
if (choixjoueur=="b1"):
     tab2[0]=1
if (choixjoueur=="b2"):
     tab2[1]=1
if (choixjoueur=="b3"):
    tab2[2]=1
if (choixjoueur=="c1"):
     tab3[0]=1
if (choixjoueur=="c2"):
    tab2[1]=1
if (choixjoueur=="c3"):
     tab3[0]=1

if (choixjoueur=="a1"):
    tab1[0]=2  

    if (choixjoueur=="a2"):
        tab1[1]=2
        if (choixjoueur=="a3"):
            tab1[2]=2
        if (choixjoueur=="b1"):
            tab2[0]=2
        if (choixjoueur=="b2"):
            tab2[1]=2
        if (choixjoueur=="b3"):
            tab2[2]=2
        if (choixjoueur=="c1"):
            tab3[0]=2
        if (choixjoueur=="c2"):
            tab2[1]=2
        if (choixjoueur=="c3"):
            tab3[0]=2
#placementj1
if(tab1[0]==1):
    ligne1='|X|-|-|' 
if(tab2[0]==1):
    ligne2='|X|-|-|' 
if(tab3[0]==1):
    ligne3='|X|-|-|'
if(tab1[1]==1):
    ligne1='|-|X|-|' 
if(tab2[1]==1):
    ligne2='|-|X|-|'
if(tab3[1]==1):
    ligne3='|-|X|-|' 
if(tab1[2]==1):
    ligne1='|-|-|X|' 
if(tab1[2]==1):
    ligne2='|-|-|X|' 
if(tab1[2]==1):
    ligne3='|-|-|X|'




#placement j2
if(tab1[0]==1):
    ligne1='|O|-|-|' 
if(tab2[0]==1):
    ligne2='|O|-|-|' 
if(tab3[0]==1):
    ligne3='|O|-|-|'
if(tab1[1]==1):
    ligne1='|-|O|-|' 
if(tab2[1]==1):
    ligne2='|-|O|-|'
if(tab3[1]==1):
    ligne3='|-|O|-|' 
if(tab1[2]==1):
    ligne1='|-|-|O|' 
if(tab1[2]==1):
    ligne2='|-|-|O|' 
if(tab1[2]==1):
    ligne3='|-|-|O|'
#3)
#check colonne j1
if(tab1[0]==1&tab2[0]==1&tab3[0]==1):
    #doit return que la colonne est complete
    if(tab1[1]==1&tab2[1]==1&tab3[1]==1):
   
        if(tab1[2]==1&tab2[2]==1&tab3[2]==1):
#check de ligne j1
if(tab1[0]==1&tab1[1]==1&tab1[2]==1):
    #doit return que la ligne est complete
    if(tab2[0]==1&tab2[1]==1&tab2[2]==1):
   
        if(tab3[2]==1&tab3[2]==1&tab3[2]==1):
#check diagonale
if(tab1[0]==1&tab2[1]==1&tab3[2]==1):
    #doit return que la diagonale est complete
    if(tab1[2]==1&tab2[1]==1&tab3[0]==1):
#4) vérifier si la grille est complete
        for i in range(len(tab1)):
            if(tab1[i]!=0):
                if(tab2[i]!=0):
                    if(tab3[i]!=0):
                        print('la grille est complete')
#6) Il faut pour programmer un puissance 4 avoir un tableau a deux dimensions aux bonnes dimensions, puis programmer une fonction qui lorsque un joueur joue dans une colonne fais descendre le pion jusqu'a rencontré un obstacle dans la colonne.