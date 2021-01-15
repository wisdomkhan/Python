#include <stdio.h>
int main(){
int i,t,n,k,d;
scanf("%d", &t);
while(t!=0){
  int sm = 0;
  scanf("%d %d %d",&n, &k, &d);
  int a[n];
  for(i=0; i<n; i++){
    scanf("%d", &a[i]);
    sm += a[i];
  }
  if(sm/k <= d)
    printf("%d\n", sm/k);
  else
    printf("%d\n", d);
  t--;
}
return 0;
}
