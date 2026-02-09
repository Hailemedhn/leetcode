from typing import List

class Solution:
    def findMedian(self, lst: List[int]) -> float:
        if len(lst) % 2 != 0:
            return lst[len(lst)//2]
        else:
            return (lst[len(lst)//2] + lst[len(lst)//2 - 1]) / 2

    def findGreaterThanMedian(self,lst: List[int]) -> int:
        if len(lst) % 2 == 0:
            return len(lst) // 2 - 1
        else:
            return len(lst) // 2
    def findLessThanMedian(self,lst: List[int]) -> int:
        if len(lst) % 2 == 0:
            return len(lst) // 2 - 1
        else:
            return len(lst) // 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shortList = nums1 if len(nums1) < len(nums2) else nums2
        longList = nums2 if nums1 is shortList else nums1
        while len(shortList) > 1:
            if len(shortList) == 2 or len(longList) == 2:
                return self.findMedian(sorted(shortList + longList))
            medianShortList = self.findMedian(shortList)
            medianLongList = self.findMedian(longList)
            if medianShortList < medianLongList:
                cut = min(self.findGreaterThanMedian(shortList), self.findLessThanMedian(longList))
                shortList = shortList[cut:]
                longList = longList[:-cut]
            elif medianShortList > medianLongList:
                cut = min(self.findGreaterThanMedian(shortList), self.findLessThanMedian(longList))
                shortList = shortList[:-cut]
                longList = longList[cut:]
            else:
                return medianShortList
        else:
            if len(shortList) == 1:
                return self.findMedian(sorted(shortList + longList))
            else:
                return self.findMedian(longList)