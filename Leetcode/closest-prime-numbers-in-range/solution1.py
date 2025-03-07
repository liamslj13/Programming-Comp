class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # review later
        def sieve(n):
            prime = [True for i in range(n+1)]
            p=2
            prime[0] = False
            prime[1] = False
            while (p*p <= n):
                if prime[p] == True:
                    for i in range(p *p, n+1, p):
                        prime[i] = False
                p += 1

            return prime

        prime = sieve(right+1)
        primeDist = []
        pair = [-1,-1]
        min = float("inf")
        flag = False
        while left <= right:
            if prime[left]:
                prime1 = left
                left += 1
                while not prime[left]:
                    if left + 1 >= len(prime)-1:
                        flag = True
                        break
                    left += 1
                if flag:
                    break
                prime2 = left
                if prime2 > right:
                    continue
                primeDist.append([prime1, prime2, prime2 - prime1])
                continue
            left += 1

        for i in range(len(primeDist)):
            if primeDist[i][2] < min:
                min = primeDist[i][2]
                pair = [primeDist[i][0], primeDist[i][1]]

        return pair
