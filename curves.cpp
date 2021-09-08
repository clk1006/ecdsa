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
        point getPoint(double,bool);
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
    const double mSec=(p2.y-p1.y)/(p2.x-p1.x);
    const double bSec=p1.y-mSec*p1.x;
    double polyn[4]={1,-pow(mSec,2),a-2*mSec*bSec,b-pow(bSec,2)};
    const double zeros[3]={getZeros(polyn)[0],getZeros(polyn)[1],getZeros(polyn)[2]};
    for(int i=0;i<3;i++){
        if(zeros[i]!=NULL&&zeros[i]!=p1.x&&zeros[i]!=p2.x){
            pEnd.x=zeros[i];
            pEnd.y=-(mSec*pEnd.x+bSec);
        }
    }
    return pEnd;
}
point eCurve::multiply(point p, int factor){
    if(factor==1) return p;
    if(factor==0) return {x:NULL,y:NULL};
    point pEnd;
    double t=pow(p.x,2);
    const double slope=0.5*(3*pow(p.x,2)-2)/(sqrt(pow(p.x,3)-2*p.x+2));
    const double mTan=p.y>0?slope:-slope;
    const double bTan=p.y-mTan*p.x;
    double polyn[4]={1,-pow(mTan,2),a-2*mTan*bTan,b-pow(bTan,2)};
    const double zeros[3]={*(getZeros(polyn)+0),*(getZeros(polyn)+1),*(getZeros(polyn)+2)};
    for(int i=0;i<3;i++){
        if(zeros[i]!=NULL&&zeros[i]!=p.x){
            pEnd.x=zeros[i];
            pEnd.y=-(mTan*pEnd.x+bTan);
        }
    }
    for(int i=3;i<=factor;i++){
        pEnd=add(pEnd,p);
    }
    return pEnd;
}
point eCurve::getPoint(double x,bool isPositive){
    double y=sqrt(pow(x,3)+a*x+b);
    if(isPositive) return {x:x,y:y};
    return {x:x,y:-y};
}
int main(){
    eCurve curve(-2,2);
    point p=curve.getPoint(0.75,true);
    point q=curve.multiply(p,2);
    point h={x:1,y:2};
}