#include <stdio.h>
int main()
{
    int num1, num2;
    printf("Enter the two numbers: ");
    scanf("%d %d", &num1, &num2);

    printf("Sum : %d\n", num1 + num2);
    printf("Difference : %d\n", num1 - num2);
    printf("Product : %d\n", num1 * num2);
    printf("Divison : %.2f\n", (float)num1/num2);

    return 0;
}