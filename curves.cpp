#include <math.h>
using namespace std;
struct point{
    int x,y;
};
class eCurve{
    private:
        int a,b;
        int order;
    public:
        eCurve(int,int,int);
        point add(point,point);
        point multiply(point,int);
        bool isOn(point);
        point getPoint(int,bool);
};
eCurve::eCurve(int aParam,int bParam,int orderParam){
    a=aParam;
    b=bParam;
    order=orderParam;
}
bool eCurve::isOn(point p){
    return (pow(p.y,2)==pow(p.x,3)+a*p.x+b);
}
point eCurve::add(point p1,point p2){
    point pAdd;
    if(p1.x==NULL&&p1.y==NULL) return p2;
    if(p2.x==NULL&&p2.y==NULL) return p1;
    if(!(isOn(p1)&&isOn(p2))){
        return {NULL};
    }
    const double lambda=((p1.x==p2.x)&&(p1.y==p1.y))?(3*pow(p1.x,2)+a)/(2*p1.y):(p1.y-p2.y)/(p1.x-p2.x);
    pAdd.x=-p1.x-p2.x+pow(lambda,2);
    pAdd.y=-p1.y+lambda*(p1.x-pAdd.x);
    return pAdd;
}
point eCurve::multiply(point p, int factor){
    switch (factor){
        case 0: return {NULL};
        case 1: return p;
        //case 2:
        default: return add(p,multiply(p,factor-1));
    }
}
point eCurve::getPoint(int x,bool isPositive){
    double y=sqrt(pow(x,3)+a*x+b);
    if((double)(int)y==y){
        if(isPositive) return {x:x,y:(int)y};
        return {x:x,y:order-(int)y};
    }
    return {NULL};
}
int main(){
    eCurve curve(-3,3,19);
    point p=curve.getPoint(-2,true);
    for(int i=0;i<10;i++){
        point q=curve.multiply(p,i);
        point h=q;
    }
}