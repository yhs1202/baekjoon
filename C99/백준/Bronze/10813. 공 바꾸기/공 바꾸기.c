#include <stdio.h>
#include <stdlib.h>
int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    // initialize array 1 to N
    int *basket = (int *)malloc(N * sizeof(int));
    if (basket == NULL) exit(1);
    for (int i = 0; i < N; i++) {
        basket[i] = i + 1;
    }
    
    // swap process with M
    for (int j = 0; j < M; j++) {
        int temp;
        int a, b;
        scanf("%d %d", &a, &b);

        temp = basket[a-1];
        basket[a-1] = basket[b-1];
        basket[b-1] = temp;
    }

    // print
    for (int i = 0; i < N; i++) {
        printf("%d ", basket[i]);
    }

    return 0;
}