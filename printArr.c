#include <stdio.h>
int main(){
  int i, t, n;
  scanf("%d", &t);
  for(i=0; i<t; i++){
    scanf("%d", &n);
    int a[n];
    for(int j = 0; j<n; j++){
      scanf("%d", &a[j]);
    }
    for(int j =0; j<n; j++){
      printf("%d ", a[j]);
    }
    printf("\n");
  }
}
