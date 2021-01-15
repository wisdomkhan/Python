#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
    int i;
    char *s;
    int c=0;
    int n[]={'0','1','2','3','4','5','6','7','8','9'};
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    int f[10] = {0};
    for(i=0;i<10;i++){
        for(int j=0;j<strlen(s);j++){
            if(n[i] == *(s+j)){
                f[i] = ++c;
            }
        }
        c = 0;
    }
    for(i=0;i<10;i++){
        printf("%d ", f[i]);
    }
}