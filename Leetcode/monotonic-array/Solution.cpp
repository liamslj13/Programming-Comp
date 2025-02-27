// https://leetcode.com/problems/monotonic-array

class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool dec = false;
        if (nums.size() == 1) {
            return true;
        } 
        if (nums[1]<nums[0]) {
            dec = true;
        } else if (nums[1] == nums[0]) {
            if (nums[nums.size()-1]<nums[0]) {
                dec = true;
            }
        }

        if (dec) {
            for (int i=1;i<nums.size();i++) {
                if (nums[i]>nums[i-1]) {
                    return false;
                }
            }
        } else {
            for (int i=1;i<nums.size();i++) {
                if (nums[i]<nums[i-1]) {
                    return false;
                }
            }
        }


        return true;
    }
};