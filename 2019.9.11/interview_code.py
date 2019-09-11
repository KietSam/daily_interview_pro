class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(',
                   '}': '{',
                   ']': '['}
        for c in s:
            if c in mapping:
                if len(stack) == 0:
                    return False
                k = stack.pop()
                if k != mapping[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
