// https://leetcode.com/problems/max-consecutive-ones

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int top = 0;
        int count = 0;

        for (int num : nums) {
            if (num == 1) {
                count++;
                if (count > top) {
                    top = count;
                }
            } else {
                count = 0;
            }
        };

        return top;
    }
};