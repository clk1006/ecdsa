from math import *
from typing import NoReturn
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __ne__(self,other):
        return self.x!=other.x or self.y!=other.y
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
class eCurve:
    def __init__(self,a,b,order):
        self.a=a
        self.b=b
        self.order=order
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
    def add(self,p,q):
        if p==point(0,0):
            return q
        if q==point(0,0):
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
