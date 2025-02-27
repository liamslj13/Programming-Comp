// https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) {
            return "";
        }
        int len1,len2;
        string build = "";

        len1 = str1.length();
        len2 = str2.length();

        int g = gcd(len1, len2);
        for (int i = 0; i < g; i++) {
            build += str2[i];
        }

        return build;
    }

    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }

        return gcd(b, a%b);
    }
};