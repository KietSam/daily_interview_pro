class Solution:
    def longestPalindrome(self, s):
        l = len(s)
        self.dp = [[None for i in range(l)] for j in range(l)]
        self.s = s

        # print(self.opt(0, l - 1))
        #
        # for arr1 in self.dp:
        #     print(arr1)

        i, j = self.opt(0, l - 1)

        return self.s[i:j+1]

    def is_palindrome_substring(self, i, j):
        # print(i, j)
        for k in range(j - i):
            if self.s[i + k] != self.s[j - k]:
                return False
        return True

    def opt(self, i, j):
        if i > j:
            return ""
        if self.dp[i][j] is not None:
            return self.dp[i][j]
        elif self.is_palindrome_substring(i, j):
            self.dp[i][j] = (i, j)
        else:
            i1, j1 = sub1 = self.opt(i+1, j)
            i2, j2 = sub2 = self.opt(i, j-1)
            self.dp[i][j] = sub1 if (j1 - i1) >= (j2 - i2) else sub2
        return self.dp[i][j]


# Fill this in.

# Test program
# s = "tracecars"
# s = "eabcb"
# s = "abadd"
s = "mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd"
print(str(Solution().longestPalindrome(s)))
# racecar