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
    def __hash__(self):
        return hash((self.x,self.y))
    def __sub__(self,other):
        return point(self.x-other.x,self.y-other.y)
    def __add__(self,other):
        return point(self.x+other.x,self.y+other.y)
    def __mod__(self,n):
        return point(self.x%n,self.y%n)
PNULL=point(-1,-1)
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
        self.storage={}
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
    def mirror(self,p):
        return point(p.x,self.order-p.y)%self.order
    def checkPoint(self,p):
        return (p.y**2)%self.order==(p.x**3+self.a*p.x+self.b)%self.order
    def add(self,p,q):
        if p==PNULL:
            return q
        if q==PNULL:
            return p
        if p==q:
            for i in range(self.order):
                if isinstance(self.getPoint(i,False),point):
                    q=self.getPoint(i,False)
            return self.mirror(self.add(q,self.mirror(self.add(p,self.add(p,q)))))
        step=q-p
        q=(q+step)%self.order
        while not self.checkPoint(q):
            q=(q+step)%self.order
        if q==p:
            return PNULL
        return self.mirror(q)
    def multiply(self,p,factor):
        if p not in self.storage.keys():
            self.storage[p]={}
        if factor in self.storage[p].keys():
            return self.storage[p][factor]
        returnV=0
        if factor==0:
            returnV=PNULL
        elif factor==1:
            returnV= p
        elif factor%2==0:
            returnV= self.add(self.multiply(p,factor/2),self.multiply(p,factor/2))
        else:
            returnV=self.add(self.multiply(p,(factor-1)/2),self.multiply(p,(factor+1)/2))
        self.storage[p][factor]=returnV
        return returnV
    def getN(self,p):
        n=2
        while(self.multiply(p,n)!=PNULL):
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
        if Q==PNULL:
            return False
        if not self.checkPoint(Q):
            return False
        if self.multiply(Q,n)!=PNULL:
            return False
        if not 0<r<n and 0<s<n:
            return False
        z=getZ(m,n)
        u1=(z/s)%n
        u2=(r/s)%n
        p=self.add(self.multiply(G,u1),self.multiply(Q,u2))
        if p==PNULL:
            return False
        if r%n!=p.x%n:
            return False
        return True
c=eCurve(5,7,29)
p=c.getPoint(4,False)