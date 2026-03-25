// main.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


struct T {
    char s[64];
    unsigned int i;
};


void f(char *input) {
    struct T t;

    // Initialize `t`.
    memset(t.s, 0, sizeof(t.s));
    t.i = 0xdeadbeef;

    printf("Address of t.s: %p\n", (void*) & t.s);
    printf("Address of t.i: %p\n", (void*) & t.i);
    printf("Size of t: %lu\n", sizeof(struct T));
    printf("Value of T.i: 0x%08x\n", t.i);

    // Copy user input in `t.s`.
    strcpy(t.s, input);

    printf("Value of T.i: 0x%08x\n", t.i);
}


int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }
    f(argv[1]);
    return 0;
}
