class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                temp = []
                while stack and stack[-1] != "[":
                    temp.append(stack.pop())
                stack.pop()

                temp.reverse()
                nums = []
                while stack and stack[-1].isdigit():
                    nums.append(stack.pop())

                nums.reverse()
                num = int(''.join(nums))
     
                stack.append((''.join(temp)) * num)
            else:
                stack.append(s[i])

        return ''.join(stack)