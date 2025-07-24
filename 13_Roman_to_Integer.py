class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):  # From left to right
            value = roman[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

# Example
sol = Solution()
print(sol.romanToInt("IX"))   # 9
print(sol.romanToInt("LVIII")) # 58
print(sol.romanToInt("MCMXCIV")) # 1994
