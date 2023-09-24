#include <stdio.h>

int main(void) {
    int a = 12;
    double x;
    printf("Input real x: ");
    scanf("%lf", &x);
    printf("a=%5d=%05d\n", a, a);
    printf("x=%f=%.3f=%6.2f=%e\n", x, x, x, x);
    return 0;
}