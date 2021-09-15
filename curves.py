from math import *
from typing import NoReturn
from random import randint
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __ne__(self,other):
        return self.x!=other.x or self.y!=other.y
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __str__(self):
        return "("+str(self.x)+"|"+str(self.y)+")"
def getZ(m,n):
    bitLen=int(log2(n))+1
    e=hash(m)
    if(e<0):
        return int(str(bin(e))[3:bitLen+3],2)
    return int(str(bin(e))[2:bitLen+2],2)
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
    def getN(self,p):
        n=2
        while(self.multiply(p,n)!=point(0,0)):
            n+=1
        return n
    def createSignature(self,G,n,d,m):
        z=getZ(m,n)
        while True:
            k=randint(1,n-1)
            p=self.multiply(G,k)
            r=p.x%n
            if r==0:
                continue
            s=((z+r*d)/k)%n
            if s==0:
                continue
            return (r,s)
    def checkSignature(self,G,n,Q,m,sig):
        (r,s)=sig
        if Q==point(0,0):
            return False
        if (Q.y**2)%self.order!=(Q.x**3+self.a*Q.x+self.b)%self.order:
            return False
        if self.multiply(Q,n)!=point(0,0):
            return False
        if not 0<r<n and 0<s<n:
            return False
        z=getZ(m,n)
        u1=(z/s)%n
        u2=(r/s)%n
        p=self.add(self.multiply(G,u1),self.multiply(Q,u2))
        if p==point(0,0):
            return False
        if r%n!=p.x%n:
            return False
        return True

