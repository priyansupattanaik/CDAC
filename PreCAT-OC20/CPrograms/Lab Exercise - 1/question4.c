#include <stdio.h>
int main()
{
    float num1, num2, num3;
    printf("Enter the three integers:");
    scanf("%d %f %f", &num1, &num2, &num3);
    printf("Average : %.2f", (num1+num2+num3)/3);
    return 0;
}