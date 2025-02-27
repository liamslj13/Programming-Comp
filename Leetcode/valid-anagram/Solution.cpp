// https://leetcode.com/problems/valid-anagram

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }
        unordered_map<char, int> sd, td;
        for (int i = 0; i<s.length(); i++) {
            if (sd.find(s[i]) != sd.end()) {
                sd[s[i]] += 1;
            } else {
                sd[s[i]] = 1;
            }

            if (td.find(t[i]) != td.end()) {
                td[t[i]] += 1;
            } else {
                td[t[i]] = 1;
            }
        }

        return td == sd;
    }
};