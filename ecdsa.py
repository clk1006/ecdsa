from curves import *
def getN(curve,p):
    i=2
    while(curve.multiply(p,i)!=point(0,0)):
        i+=1
    return i
curve=eCurve(-3,5,19)
p=curve.getPoint(3,False)
print(getN(curve,p))
