#include <math.h>
#include "math.cpp"
using namespace std;
struct point{
    double x,y;
};
class eCurve{
    private:
        int a,b;
    public:
        eCurve(int,int);
        point add(point,point);
        point multiply(point,int);
        bool isOn(point);
};
eCurve::eCurve(int aParam,int bParam){
    a=aParam;
    b=bParam;
}
bool eCurve::isOn(point p){
    return (pow(p.y,2)==pow(p.x,3)+((double)a)*p.x+b);
}
point eCurve::add(point p1,point p2){
    point pEnd;
    if(!(isOn(p1)&&isOn(p2))){
        return pEnd;
    }
    double mSec=(p2.y-p1.y)/(p2.x-p1.x);
    double bSec=p1.y-mSec*p1.x;
    double polyn[4]={1,-pow(mSec,2),a-2*mSec*bSec,b-pow(bSec,2)};
    double zeros[3]={getZeros(polyn)[0],getZeros(polyn)[1],getZeros(polyn)[2]};
    for(int i=0;i<3;i++){
        if(zeros[i]!=NULL&&zeros[i]!=p1.x&&zeros[i]!=p2.x){
            pEnd.x=zeros[i];
            pEnd.y=-(mSec*pEnd.x+bSec);
        }
    }
    return pEnd;
}