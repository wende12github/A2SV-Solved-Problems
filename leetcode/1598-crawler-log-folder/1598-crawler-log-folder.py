class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for dirs in logs:
            if dirs == "../":
                if stack:
                    stack.pop()
            elif dirs != "./":
                stack.append(dirs)
        return len(stack)