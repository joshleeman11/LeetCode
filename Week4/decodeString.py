class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                decodedString = ""
                while stack and stack[-1] != "[":
                    decodedString = stack.pop() + decodedString
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * decodedString)
        return "".join(stack)
            
sol = Solution()
print(sol.decodeString("3[a]2[bc]"))