#include <stdio.h>
#include <math.h>

int main(void) 
{
    float a, x, g, f, y;
    printf("Vvedite a: ");
    scanf("%f", &a);
    printf("Vvedite x: ");
    scanf("%f", &x);
    g = - (16 * a * a + 24 * a * x - 27 * x * x) / (45 * a * a - 29 * a * x + 4 * x * x);
    printf("G=%f\n\n", g);

    printf("Vvedite a: ");
    scanf("%f", &a);
    printf("Vvedite x: ");
    scanf("%f", &x);
    f = -atan(10 * a * a + 13 * a * a - 30 * x * x);
    printf("F=%f\n\n", f);

    printf("Vvedite a: ");
    scanf("%f", &a);
    printf("Vvedite x: ");
    scanf("%f", &x);
    y = log(2 * a * a + 19 * a * x + 9 * x * x + 1) / log(10);
    printf("Y=%f\n\n", y);
}
