class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfLongestStringWithoutRepeating = 0
        longestStringWithoutRepeating = ""
        i = 0
        while i < len(s):
            if s[i] not in longestStringWithoutRepeating:
                longestStringWithoutRepeating += s[i]
            else:
                if len(longestStringWithoutRepeating) > lengthOfLongestStringWithoutRepeating:
                    lengthOfLongestStringWithoutRepeating = len(longestStringWithoutRepeating)
                if len(longestStringWithoutRepeating) == 1:
                    pass
                else:
                    longestStringWithoutRepeating = longestStringWithoutRepeating[1:]
                    i -= 1
            i += 1
        return max(lengthOfLongestStringWithoutRepeating, len(longestStringWithoutRepeating))