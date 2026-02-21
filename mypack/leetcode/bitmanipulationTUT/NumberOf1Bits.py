class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for _ in range(32):
            if (n & 1) == 1:
                count += 1
            n >>= 1
        return count


# Create object
sol = Solution()

# Call method and print result
print(sol.hammingWeight(5))  # 5 -> 101 (binary) what is self n :int
