class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfLongestStringWithoutRepeating = 0
        longestStringWithoutRepeating = ""
        i,jumpIndex = 0,0
        stringDict = {i:s[i] for i in range(len(s))}
        print(stringDict)

        while i < len(s):
            if s[i] not in longestStringWithoutRepeating:
                longestStringWithoutRepeating += s[i]
            else:
                if len(longestStringWithoutRepeating) > lengthOfLongestStringWithoutRepeating:
                    lengthOfLongestStringWithoutRepeating = len(longestStringWithoutRepeating)
                
                jumpIndex = longestStringWithoutRepeating.index(s[i]) + 1
                longestStringWithoutRepeating = longestStringWithoutRepeating[jumpIndex:]
                continue
            i +=  1

        return max(lengthOfLongestStringWithoutRepeating, len(longestStringWithoutRepeating))