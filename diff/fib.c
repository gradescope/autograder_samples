#include <stdio.h>
#include <stdlib.h>

int fib(int n) {
    if (n <= 2){
        return 1;
    }
    return fib(n-1) + fib(n-2);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        fprintf(stderr, "Error: Insufficient arguments.\n");
        return -1;
    }
    int arg = atoi(argv[1]);
    printf("%d\n", fib(arg));
    return 0;
}
