#include <stdio.h>
#include <math.h>

int main(void) {
    float a, x, g, f, y;
    int number;

    printf("Vvedite n: ");
    scanf("%i", &number);

    switch (number)
    {
        case 1:
            printf("Vvedite a: ");
            scanf("%f", &a);
            printf("Vvedite x: ");
            scanf("%f", &x);
            g = - (16 * a * a + 24 * a * x - 27 * x * x) / (45 * a * a - 29 * a * x + 4 * x * x);
            printf("G=%f\n\n", g);
        case 2:
            printf("Vvedite a: ");
            scanf("%f", &a);
            printf("Vvedite x: ");
            scanf("%f", &x);
            f = -atan(10 * a * a + 13 * a * a - 30 * x * x);
            printf("F=%f\n\n", f);
        case 3:
            printf("Vvedite a: ");
            scanf("%f", &a);
            printf("Vvedite x: ");
            scanf("%f", &x);
            if ((2 * a * a + 19 * a * x + 9 * x * x + 1) >= 0)
            {
                y = log(2 * a * a + 19 * a * x + 9 * x * x + 1) / log(10);
                printf("Y=%f\n\n", y);
            }
            else
            {
                printf("Log otricatelen =(\n");
                break;
            }
        default:
            printf("Vi vveli nepravilnoe chislo :(\n");
    }
}
