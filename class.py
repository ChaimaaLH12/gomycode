from math import sqrt
print("Question 1 : ")
class Point3D() :
    def __init__(self,x, y,z):
        self.x = x
        self.y = y
        self.z = z
    def Return(self):
        print(f"({self.x},{self.y},{self.z}) ")
My_Point= Point3D(1,2,3)
My_Point.Return()
print("---------------------------------------------------")
print("Question 2 : ")
class Rectangle() :
    def __init__(self,length, width):
        self.len = length
        self.wid = width
    def Aria(self):
        A = self.wid * self.len
        print(f"The area est :{self.wid} * {self.len} = {A}")
    def  Perimeter(self):
        P = (self.wid+self.len)*2
        print(f"The Perimeter est :({self.wid}+{self.len})*2 = {P}")
My_Rectangle =Rectangle(4,3)
My_Rectangle.Aria()
My_Rectangle.Perimeter()
print("---------------------------------------------------")
print("Question 3 : ")
class Cercle():
    def __init__(self,x,y,R):
        self.x = x
        self.y = y
        self.rayon=R
    def Aria(self):
        Pi = 3.14
        A = (self.rayon**2)* Pi
        print(f"The area est : ({self.rayon}**2)* {Pi}= {A}")
    def  Perimeter(self):
        pi = 3.14
        P = (self.rayon)*2*pi
        print(f"The Perimeter est : {self.rayon}*2*{pi} = {P}")
    def Inside(self, x, y) :
        
        D =((x-self.x)**2+(y-self.y)**2)
        print(D)
        if D < self.rayon :
            print("le Point est a l'interireur de cercle")
        else:
            print("le Point est a l'extirieur de la cercle ")

C1 = Cercle(0,0,3)
C2 = Cercle(1,1,4)
C1.Aria()
C1.Perimeter()
C1.Inside(5, 8)
print("---------------------------------------------------")
print("Question 4 : ")
#deposit and withdraw
class Bank():
    def __init__(self,B):
        self.B =B
        self.sal=0
    def deposit(self,m):
        N=self.sal+m
        self.sal=N
        print("new sal est :",N)
    def withdraw(self, m):
        if self.sal<m :
            print("solde insuffisant !")
        else :
            N=self.sal-m
            self.sal=N
            print("new solde est : ",N)
B=Bank("ggdg")
B.deposit(10000)
B.withdraw(234)
