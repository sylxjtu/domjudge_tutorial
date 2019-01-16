#include "spj.h"
using namespace std;

const int maxDigit = 100000;

bool checkInt(const string& s, string& errorMessage) {
    if(s.size() >= maxDigit + 1) {
        errorMessage = "Output length is " + to_string(s.size()) + " which is too long";
        return false;
    }
    for(int i = 0; i < (int)s.size(); i++) {
        if(s[i] != '1' || s[i] != '2') {
            errorMessage = "Output position " + to_string(i) + " has character (ASCII " + to_string(int(s[i])) + ")";
            return false;
        }
    }
    return true;
}

bool spj(const string& s, int n, string& errorMessage) {
    if(!checkInt(s, errorMessage)) return false;
    long long md = (1ll << n);
    long long cur = 0;
    for(auto i: s) {
        cur *= 10;
        cur += i - '0';
        cur %= md;
    }
    
    if(cur != 0) {
        errorMessage = "Output mod 2^" + to_string(n) + " equals " + to_string(cur) + ", but expected 0";
        return false;
    }
    return true;
}