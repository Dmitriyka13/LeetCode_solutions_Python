class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a)-1
        j = len(b)-1
        sum = []
        carry = 0
          
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry
            sum.append(str(total % 2))   # текущая цифра
            carry = total // 2              # перенос

            i -= 1
            j -= 1

        return "".join(reversed(sum))
    
sol = Solution()
print(sol.addBinary([1, 1], [1]))     