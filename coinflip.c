#include <stdio.h>
int main(){
  int T, g, face, q, n;
  scanf("%d", &T);
  for(int i=0; i<T; i++){
    scanf("%d", &g);
    for(int j=0; j<g; j++){
      scanf("%d %d %d", &face, &n, &q);
      if(n % 2 == 0)
        printf("%d\n", (n/2));
      else{
        if(face == 1){
          if(q == 2)
            printf("%d\n", (n/2) + 1);
          else
            printf("%d\n", n/2);
        }
        else if(face == 2){
          if(q == 1)
            printf("%d\n", (n/2) + 1);
          else
            printf("%d\n", n/2);
        }
      }
    }
  }
  return 0;
}
