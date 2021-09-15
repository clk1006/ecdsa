from curves import *
def getN(curve,p):
    i=2
    while(curve.multiply(p,i)!=point(0,0)):
        i+=1
    return i
print(point(0,0)==point(0,0))
