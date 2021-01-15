#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int count4(char s){
    int four = 0;
    for(int i=0; i<strlen(s); i++){
        if(s[i] == '4'){
            ++four;
        }
    }
    return four;
}
int main(){
    int t;
    scanf("%d", &t);
    char s;
    //s = malloc(1024 * sizeof(char));
    int op[t];
    for(int i=0; i<t; i++){
        scanf("%[^\n]", &s);
        printf("%[^\n]", s);
        op[i] = count4(s);
    }
    for(int i=0; i<t; i++){
        printf("%d\n", op[i]);
    }
}