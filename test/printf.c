// RUN: clang -target arm-linux-gnueabihf -march=v7m -mthumb -c %s -o %t.o
// RUN: llvm-jitlink %s | Filecheck %s

// CHECK: 42
int printf(const char *fmt, ...);
int main() {
    printf("%d\n", 42);
    return 0;
}
