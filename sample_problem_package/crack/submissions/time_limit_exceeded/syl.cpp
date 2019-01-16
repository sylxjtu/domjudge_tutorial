#include <bits/stdc++.h>
using namespace std;

bool check(const string& s) {
    for(auto c: s) if(c != '1') return false;
    return true;
}

int main() {
    while(1);
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;
    int cnt = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 1; j <= m && i + j <= n; j++) {
            if(check(s.substr(i, j))) cnt++;
        }
    }
    cout << cnt << endl;
}