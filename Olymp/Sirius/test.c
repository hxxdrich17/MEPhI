#include <stdio.h>

int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    int z = 2 * (x + y);
    char arr[3][1];
    sprintf(arr[0], "%d", x);
    sprintf(arr[1], "%d", y);
    sprintf(arr[2], "%d", z);
    for (int i = 0; i < 3; i++) {
        printf("%c:%5o%5d%5x\n", arr[i][0], arr[i][0], arr[i][0], arr[i][0]);
    }
    return 0;
}