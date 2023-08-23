# Question 1 :
#Write a Python program that multiplies all the items in a list.
print("Question 1 :")
L = [2,3,4,5,6] #720
Res = 1
for i in L :
    Res=Res*i
print(Res)
print("----------------------------------------------------------------------")
# Question 2 : 
print("Question 2 :")
from operator import itemgetter
L1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
k=sorted(L1,key=itemgetter(1))
print(k)
print("----------------------------------------------------------------------")
#Question 3 :
print("Question 3 :")
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d2:
    if key in d1:
        d2[key] = d2[key] + d1[key]
    else:
        pass    
print(d2)
print("----------------------------------------------------------------------")
#Question 4 :
print("Question 4 :")
#if n =8 result : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
n= int(input("combien de fois : "))
dict = {}
for i in range(1, n+1):
    dict[i] = i*i
print(dict)
print("----------------------------------------------------------------------")
#Question 5 :
print("Question 5 :")
tuble = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(tuble, key=lambda x: float(x[1]), reverse=True))
print("----------------------------------------------------------------------")
#Question 6 :
print("Question 6 :")
#Write a Python program to create a set.
List = set()
n = int(input(" entrez le nombre des elements a ajouter a la liste : n = "))
print(n)
for i in range(0,n) : 
    m = int(input(f" l'element {i+1} "))
    List.add(m) 
print(List)
for i in List:
    print(i)
#remove items from a given set
x2 = int(input(" l'element que vous voulez retirer : "))
List.remove(x2)
print(List)
