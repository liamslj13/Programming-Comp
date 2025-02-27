// https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(num: int) -> int:
            if num > 0:
                return 1
            elif num < 0:
                return -1
            return 0

        product = 1
        for num in nums:
            product *= num

        return signFunc(product)
        
        