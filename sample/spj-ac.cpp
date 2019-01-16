#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; scanf("%d", &n);
    while(n--) {
        double x;
        scanf("%lf", &x);
        printf("%.10lf\n", 1 / x);
    }
    return 0;
}