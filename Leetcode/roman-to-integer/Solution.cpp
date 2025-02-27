// https://leetcode.com/problems/roman-to-integer

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> map = {
        {'I', 1}, {'V', 5}, {'X', 10}, 
        {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};

        int sum = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i + 1 < s.size()) {
                if (map[s[i + 1]] > map[s[i]]) {
                    sum -= map[s[i]];
                } else {
                    sum += map[s[i]];
                }
            } else {
                sum += map[s[i]];
            }
        }

        return sum;
    }
};