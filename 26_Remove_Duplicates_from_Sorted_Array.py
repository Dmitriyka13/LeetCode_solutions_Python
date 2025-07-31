class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k]=nums[i]
                k +=1
        for i in range(k, len(nums)):
            nums[i]= "_"
        return k 
    
sol = Solution()
nums = [1, 2, 3, 4, 4, 4, 5]
k = sol.removeDuplicates(nums)
print(nums) 
print("k =", k)  