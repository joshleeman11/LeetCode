class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        result = 0
        n = len(s)
        k=0
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        if len(s) > 0 and s[0] == "+":
            sign = 1
            k = 1 
        elif len(s) > 0 and s[0] == "-":
            sign = -1
            k = 1
            
        while k < n and s[k].isdigit():
            digit = int(s[k])
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            result = 10* result + digit
            k += 1
        return sign*result

sol = Solution()
print(sol.myAtoi("42s"))