// https://leetcode.com/problems/merge-strings-alternately

#include <iostream>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string x ="";
        int w1l = word1.length();
        int w2l = word2.length();
        int bound;
        bool flag;

        if (w1l > w2l) {
            bound = w1l;
        } else {
            bound = w2l;
            flag = true;
        }

        for (int i = 0; i < bound; i++) {
            if (flag && w1l <= i) {
                x += word2[i];
            } else if (w2l <= i) {
                x += word1[i];
            } else {
                x += word1[i];
                x += word2[i];
            }
        }

        return x;
    }
};