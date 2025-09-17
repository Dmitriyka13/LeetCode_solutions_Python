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
            sum.append(str(total % 2))   # current number
            carry = total // 2           # digit transfer

            i -= 1
            j -= 1

        return "".join(reversed(sum))
        #while i>=0 or j>=0 or carry:
        #    total = int(a[i]) + int(b[j]) + carry
        #    if total < 2:
        #        carry = 0
        #    elif total == 2:
        #        carry = 1
        #        total = 0
        #    else:
        #        carry = 1
        #        total = 1
        #    sum.append(str(total))
        #    i -=1
        #    j-=1
        #return "".join(reversed(sum))
    
sol = Solution()
print(sol.addBinary([1], [0]))     