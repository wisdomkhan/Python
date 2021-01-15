#include <stdio.h>
int m;
char grade;
scanf("%d", &m);
if(m>0 && m<39)
  grade = 'D';
else if(m>=40 && m<59)
  grade = 'C';
else if(m>=60 && m<79)
  grade = 'B';
else if(m>=80 && m<=100)
  grade = 'A';
printf("GRADE :%c ", grade);
