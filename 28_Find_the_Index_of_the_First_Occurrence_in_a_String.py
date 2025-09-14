class Solution(object):
    def strStr(self, haystack, needle):
       
        if needle == "":
            return 0
        if len(haystack) < len(needle):
            return -1
        
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
            
        return -1
    

sol = Solution()
print(sol.strStr("sadbutsad", "sad")) 
print(sol.strStr("leetcode", "leeto"))  
