class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0]

sol=Solution()
print(sol.longestCommonPrefix(["flower", "flow", "fight"])) 