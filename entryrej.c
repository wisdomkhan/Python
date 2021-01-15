#include <stdio.h>
int main(){
  int n, q;
  scanf("%d %d", &n, &q);
  int a[n];
  int pr[n*n];
  pr[0] = 0;
  for(int i=0; i<n; i++){
    int s = 0;
    scanf("%d", &a[i]);
    for(int j=0; j<=i; j++){
      s += a[j];
    }
    pr[i+1] = s;
  }
  int l, r;
  for(int i=0; i<q; i++){
    scanf("%d %d", &l, &r);
    printf("%d\n", pr[r] - pr[l-1]);
    }
  }
