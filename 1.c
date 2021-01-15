# include <stdio.h>
int main(){
float r,h,v,sa;
printf("Enter base radius and height\n");
scanf("%f %f", &r,&h);
v = 3.14*r*r*h;
sa = 2*3.14*r*(h+r);
printf("Volume = %f\nSurface Area = %f", sa,v);
return 0;
}
