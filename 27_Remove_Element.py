class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        for i in range(k, len(nums)):
            nums[i]="_"
        return k


sol = Solution()
nums = [2,2,3,3,3,2,2,1,1]
k = sol.removeElement(nums, 1)
print(nums) 
print("k =", k) 