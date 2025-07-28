class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[top] != char:
                    return False

        return not stack

r = Solution()
result = r.isValid("(())")
print(result)
