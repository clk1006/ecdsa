from math import *
from typing import NoReturn
class point:
    def __init__(self,x,y,order):
        self.x=x%order
        self.y=y%order
class eCurve:
    def __init__(self,a,b,order):
        self.a=a
        self.b=b
        self.order=order
    def getPoint(self,x,isPostive):
        y=sqrt(x**3+self.a*x+self.b)
        if int(y)==y:
            if isPostive:
                return point(x,y,self.order)
            return point(x,-y,self.order)
        return NoReturn
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
            return self.getDouble(self,p)
        return self.add(self,self.multiply(self,p,factor-1),p)
    def getDouble(self,p):
        pass