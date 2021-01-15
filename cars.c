#include <stdio.h>
int count(int n, int speeds[]){
  int x = 1;
  int m = speeds[0];
  for(int i=0; i<n;i++){
    if(speeds[i]<m){
      x++;
      m=speeds[i];
    }
  }
  return x;
}
int main(){
  int i, n, t;
  scanf("%d", &t);
  int ans[t];
  for(int p=0; p<t; p++){
    scanf("%d", &n); // inputting no of cars
    int speeds[n];
    for(i=0; i<n; i++){
      scanf("%d", &speeds[i]);
    }//i loop
  ans[p] = count(n, speeds);
  }//p loop
  for(i=0; i<t; i++){
    printf("%d\n", ans[i]);
  }
  return 0;
}
