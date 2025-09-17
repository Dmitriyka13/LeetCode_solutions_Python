class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:  # 0 or 1 the same with the result
            return x

        left = 1
        right = x // 2  # sqrt less than x//2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # there right < left, and right — floor(sqrt(x))
    
sol = Solution()
print(sol.mySqrt(8))
