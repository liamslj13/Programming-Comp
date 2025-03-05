#define ll long long

class Solution {
public:
    long long coloredCells(int n) {
        if (n == 1) {return 1;}

        ll numOfBlocks = 1;
        ll toAdd = 4;
        for (int i = 1; i < n; i++) {
            numOfBlocks += toAdd;
            toAdd += 4;
        }

        return numOfBlocks;
    }
};
