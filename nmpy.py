import numpy as np 
std=int(input("Combien d'etudiants que vous voulez saisir ? : "))
sbj=int(input("Combient de subjects que vous voulez saisir ? :"))
a = np.zeros((std,5))
print(a)
somme=np.zeros(std)
Prctg=np.zeros(std)
print(somme)
for i in range(0,std) :
    print(f'etudiant {i+1} :')
    for j in range(0,sbj):
        x=input(f'saisez le nom de subject {j+1}')
        print(f'{x}')
        a[i,j]=int(input(f" a [{i}, {j}] =  "))
        somme[i]+=a[i,j]
        Prctg[i]=(somme[i]/(sbj*100))*100
    print(f"la somme d'etudiant {i+1} est : {somme[i]}")
    print(f"la porcentage d'etudiant {i+1} est : {Prctg[i]}%")
    if Prctg[i] > 90 :
        print('A+')
    elif Prctg[i] > 80 :
        print('A')
    elif Prctg[i] > 70 :
        print('B+')
    elif Prctg[i] > 60 :
        print('B')
    elif Prctg[i] > 50 :
        print('c')
    else :
        print('F')
