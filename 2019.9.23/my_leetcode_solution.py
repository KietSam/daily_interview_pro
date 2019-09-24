class Solution:
    def helper(self, s1, s2, i1, i2):
        if (i1, i2) not in self.M:
            if i1 >= len(s1) and i2 >= len(s2):
                self.M[(i1, i2)] = 0
            elif i1 >= len(s1):
                self.M[(i1, i2)] = len(s2) - i2
            elif i2 >= len(s2):
                self.M[(i1, i2)] = len(s1) - i1
            elif s1[i1] == s2[i2]:
                self.M[(i1, i2)] = self.helper(s1, s2, i1 + 1, i2 + 1)
            else:
                self.M[(i1, i2)] = min(self.helper(s1, s2, i1 + 1, i2 + 1),
                                       self.helper(s1, s2, i1 + 1, i2),
                                       self.helper(s1, s2, i1, i2 + 1)) + 1
        return self.M[(i1, i2)]

    def minDistance(self, word1: str, word2: str) -> int:
        self.M = {}
        return self.helper(word1, word2, 0, 0)
