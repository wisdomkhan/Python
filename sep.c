#include <stdio.h>
#include <math.h>
int main(){
	double n, i, f;
	scanf("%lf", &n);
	f = modf(n, &i);
	printf("Integral part = %lf\n", i);
	printf("Fractionl part = %lf\n", f);
	return 0;
}
