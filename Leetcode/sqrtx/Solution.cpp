// https://leetcode.com/problems/sqrtx

#define ll long long

class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        ll i = 1;
        while(i * i <= x) {
            i += 1;
        }

        return i-1;
    }
};