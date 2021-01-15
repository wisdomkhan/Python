#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n, sum = 0;
    scanf("%d",&n);
    int *a = malloc(sizeof(int) * n); //dynamic array allocation
    for(int i=0; i<n; i++)
    {
        scanf("%d", &a[i]);
        sum += a[i];
    }
    printf("%d", sum);
    return 0;
}