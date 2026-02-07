

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfLongestStringWithoutRepeating = 0
        longestStringWithoutRepeating = ""
        j = 0
        while j < len(s) - lengthOfLongestStringWithoutRepeating:
            i = j
            while i < len(s) and s[i] not in longestStringWithoutRepeating:
                longestStringWithoutRepeating += s[i]
                i += 1
            if len(longestStringWithoutRepeating) > lengthOfLongestStringWithoutRepeating:
                lengthOfLongestStringWithoutRepeating = len(longestStringWithoutRepeating)
        
            longestStringWithoutRepeating = ""
            j += 1
        return lengthOfLongestStringWithoutRepeating