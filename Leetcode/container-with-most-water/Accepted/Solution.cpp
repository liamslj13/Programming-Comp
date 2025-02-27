// https://leetcode.com/problems/container-with-most-water

class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = 0;
        int lhs = 0;
        int rhs = height.size() - 1;

        while (lhs < rhs) {
            int difference = rhs - lhs;
            if (height[rhs] < height[lhs]) {
                if (difference * height[rhs] > max) {
                    max = difference * height[rhs];
                }
                rhs--;
            } else {
                if (difference * height[lhs] > max) {
                    max = difference * height[lhs];
                }
                lhs++;
            }
        }

        return max;
    }
};