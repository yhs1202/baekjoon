#include <stdio.h>
#include <stdlib.h>
int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    int *basket = (int *)calloc(N, sizeof(int));
    if (basket == NULL) exit(1);
    for (int i = 0; i < M; i++) {
        int start, end, num;
        scanf("%d %d %d", &start, &end, &num);
        for (int j = start - 1; j < end; j++) {
            basket[j] = num;
        }
    }
    for (int i = 0; i < N; i++) {
        printf("%d ", basket[i]);
    }
    free(basket);
    basket = NULL;
    return 0;
}