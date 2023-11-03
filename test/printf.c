// RUN: clang -target arm-linux-gnueabihf -march=v7a -c %s -o %t.o
// RUN: %llvm-jitlink %t.o | FileCheck %s

// CHECK: 42
int printf(const char *fmt, ...);
int main() {
    printf("%d\n", 42);
    return 0;
}
