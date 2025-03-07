class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            prime = [True] * (n + 1)
            prime[0] = prime[1] = False
            for p in range(2, int(n**0.5) + 1):
                if prime[p]:
                    for i in range(p * p, n + 1, p):
                        prime[i] = False
            return prime

        prime = sieve(right)
        prev = -1
        min = float("inf")
        result = [-1, -1]

        for num in range(left, right + 1):
            if prime[num]:
                if prev != -1 and (num - prev) < min:
                    min = num - prev
                    result = [prev, num]
                prev = num

        return result
