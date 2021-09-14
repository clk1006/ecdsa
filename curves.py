from math import *
from typing import NoReturn
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class eCurve:
    def __init__(self,a,b,order):
        self.a=a
        self.b=b
        self.order=order
    def isIdentity(self,p):
        return p.x==0 and p.y==0
    def getPoint(self,x,isBigger):
        res=(x**3+self.a*x+self.b)%self.order
        y=-1
        for i in range(int((self.order+1)/2)):
            if (i**2)%self.order==res:
                y=i
                break
        if y==-1:
            return NoReturn
        if isBigger:
            return point(x,self.order-y)
        return point(x,y)
    def check(self,p):
        return p.y**2==p.x**3+self.a*p.x+self.b
    def add(self,p,q):
        if self.isIdentity(p):
            return q
        if self.isIdentity(q):
            return p
        if p.x==q.x and p.y==self.order-q.y:
            return point(0,0)
        lam=0
        if p.x==q.x and p.y==q.y:
            lam=(3*p.x**2+self.a)/(2*p.y)
        else:
            lam=(p.y-q.y)/(p.x-q.x)
        x=-p.x-q.x+lam**2
        if x!=int(x):
            return point(0,0)
        y=-p.y+lam*(p.x-x)
        return point(x%self.order,y%self.order)
    def multiply(self,p,factor):
        if factor==0:
            return point(0,0)
        if factor==1:
            return p
        return self.add(self.multiply(p,factor-1),p)
curve=eCurve(-3,5,19)
p=curve.getPoint(0,False)
q=curve.getPoint(5,True)
r=curve.multiply(p,2)
print("Hi")