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
    def getPoint(self,x,isBigger):
        res=(x**2+self.a*x+self.b)%self.order
        y=-1
        for i in range((self.order-1)/2):
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
        pass
    def multiply(self,p,factor):
        if factor==0:
            return NoReturn
        if factor==1:
            return p
        if factor==2:
            return self.getDouble(p)
        return self.add(self.multiply(p,factor-1),p)
    def getDouble(self,p):
        q=point(0,0)
        for i in range(self.order):
            if i!=p.x and self.getPoint(i,False)!=NoReturn:
                q=self.getPoint(i,False)
        p2=self.add(p,q)
        p3=self.add(p,p2)
        p3.y=self.order-p3.y
        p4=self.add(p3,q)
        p4.y=self.order-p4.y
        return p4
