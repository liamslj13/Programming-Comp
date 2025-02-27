// https://leetcode.com/problems/n-th-tribonacci-number

class Solution {
public: 
    int f(int n, unordered_map<int, int>& cache) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else if (n == 2) { 
            return 1;
        }
        if (cache.find(n) != cache.end()) {
            return cache[n];
        }
        cache[n] = f(n-3, cache) + f(n-2, cache) + f(n-1,cache);
        return cache[n];
    }


    int tribonacci(int n) {
        unordered_map<int,int> cache;
        return f(n, cache);
    }
};