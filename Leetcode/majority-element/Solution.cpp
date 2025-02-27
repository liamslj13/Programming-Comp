// https://leetcode.com/problems/majority-element

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> map;
        int comp = -99;
        int maj = 0;

        for (int i = 0; i < nums.size(); i++) {
            map[nums[i]] += 1;
            if (map[nums[i]] > comp) {
                comp = map[nums[i]];
                maj = nums[i];
            }
        }

        return maj;
    }
};