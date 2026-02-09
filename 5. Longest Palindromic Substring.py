class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenLongestPalindrome,i = 0,0
        longestPalindrome = ""
        while i < len(s) - lenLongestPalindrome:
            j = i + lenLongestPalindrome + 1
            while j <= len(s):
                string = s[i:j]
                if string == string[::-1]:
                    if lenLongestPalindrome < j - i:
                        lenLongestPalindrome = j -i
                        longestPalindrome = string
                j += 1
            i += 1
        return longestPalindrome