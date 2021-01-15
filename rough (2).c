#include <stdio.h>
int rec(int n, int a, int b, int c){
    if(n - 3 > 0){
        c = a + b + c;
        a = b;
        b = c;
        rec(n - 1, a, b, c);
    }
    return c;
}
int main(){
    int n, a, b, c;
    scanf("%d", &n);
    scanf("%d %d %d", &a, &b, &c);
    int ans = rec(n, a, b, c); 
    printf("%d", ans); 
    return 0;
}
