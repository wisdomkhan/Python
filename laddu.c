#include <stdio.h>
int main(){
  int T, g, face, q, n,ans=0;
  scanf("%d", &T);
  scanf("%d", &g);
  for(int i=0; i<T; i++){
    for(int j=0; j<g; j++)
    {
      scanf("%d %d %d", &face, &n, &q);
      int a[n];
      for(int x=0; x<n; x++){
        a[x] = face;
      }
      for(int k=0; k<n; k++){
        int l = 0;
        while(l<=k)
        {
          if(a[l] == 0)
            a[l] = 1;
          else if(a[l] == 1)
            a[l] = 0;
          l++;
        }//while
      }//k
      for(int i=0; i<n;i++){
        if(q == face){
          if(a[i] == face)
            ans++;
        }
        else if(q == 2){
          if(a[i] != face)
            ans++;
        }
           }
      printf("%d\n", ans);
      ans = 0;
    }//j
  }//i
  return 0;
}
