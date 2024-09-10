#include <iostream>
using namespace std;

extern "C" __declspec(dllexport) int f(int n) {
    return (n == 1 || n == 0) ? 1 : f(n-1)+f(n-2);
}
int main() {
    return 0;
}