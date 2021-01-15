#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    for(int i=0; s[i] != '\0'; i++) //traversing as each word or space as a token
    {
        
        if ( s[i] == 32)
        {
            printf("\n");
        }
        else{
            printf("%c", s[i]);
        }
    }
    return 0;
}