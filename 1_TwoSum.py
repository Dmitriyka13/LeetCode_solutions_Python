class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

s=Solution()
result = s.twoSum([0,6,1,9,5,8], 11)
print(result)

