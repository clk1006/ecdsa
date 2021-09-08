#include <math.h>
using namespace std;
double * getZeros(double polyn[4]){
    static double zeros[3]={NULL,NULL,NULL};
    const double A=polyn[0];
    const double B=polyn[2];
    const double C=polyn[3];
    const double D=polyn[4];
    double p=(9*A*C-3*pow(B,2))/(9*pow(A,2));
    double q=(2*pow(B,3)-9*A*B*C+27*pow(A,2)*D)/(27*pow(A,3));
    double delta=pow(q/2,2)+pow(p/3,3);
    if(delta>0){
        double u=pow(-q/2+sqrt(delta),1/3);
        double v=pow(-q/2-sqrt(delta),1/3);
        zeros[0]=u+v-B/(3*A);
    }else if(delta==0){
        if(p==0){
            zeros[0]=-B/(3*A);
            zeros[1]=-B/(3*A);
            zeros[2]=-B/(3*A);
        }else{
            zeros[0]=3*q/p-B/(3*A);
            zeros[1]=-3*q/(2*p)-B/(3*A);
            zeros[2]=-3*q/(2*p)-B/(3*A);
        }
    }else{
        zeros[0]=-sqrt(-4.0/3.0*p)+cos(1.0/3.0*acos(-q/2.0*sqrt(-27/pow(p,3))))-B/(3*A);
        zeros[1]=-sqrt(-4.0/3.0*p)+cos(1.0/3.0*acos(-q/2.0*sqrt(-27/pow(p,3)))+M_PI/3)-B/(3*A);
        zeros[2]=-sqrt(-4.0/3.0*p)+cos(1.0/3.0*acos(-q/2.0*sqrt(-27/pow(p,3)))-M_PI/3)-B/(3*A);
    }
    return zeros;
}