class Solution:
    def lengthOfLongestSubstring(self, s):
        longest_length = 0
        for i in range(len(s)):
            set = {}
            for j in range(len(s) - i):
                c = s[i + j]
                if c in set:
                    if len(set) > longest_length:
                        longest_length = len(set)
                    break
                else:
                    set[c] = 1
        return longest_length

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
