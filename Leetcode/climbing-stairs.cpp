class Solution {
public:
    int climbStairs(int n) {
        int prev, prev2, temp;

        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }

        prev = 1;
        prev2 = 1;
        for (int i = 1; i < n; i++) {
            temp = prev;
            prev = prev2 + prev;
            prev2 = temp;
        }

        return prev;
    }
};
