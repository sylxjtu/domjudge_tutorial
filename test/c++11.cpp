#include <bits/stdc++.h>
using namespace std;

int main() {
    auto i = 1;
    vector<int> v{1, 2, 3, 4};
    for(int i = 0; i < 10; i++) {
        auto f = [](int x) {
            cout << x;
        };
        f(1);
    }
    return 0;
}
