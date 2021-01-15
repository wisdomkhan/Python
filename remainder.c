#include <stdio.h>
int main()
{
    int n, x, y, i, j;
    scanf("%d", &n);
        int op[n];
    for (i = 0; i < n; i++)
        {scanf("%d %d", &x, &y);
        op[i] = x % y;}
    for (j = 0; j < n; j++)
       { printf("%d\n", op[j]);}
    return 0;
}