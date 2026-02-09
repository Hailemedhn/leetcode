from typing import List

class Solution:
    def findMedian(self, lst: List[int], start:int, end: int) -> float:
        if (end-start) % 2 != 0:
            return lst[(end-start)//2 + start]
        else:
            return (lst[(end-start)//2 + start] + lst[(end-start)//2 - 1 + start]) / 2

    def findCut(self, start: int, end: int) -> int:
        if (end-start) % 2 == 0:
            return (end-start) // 2 - 1
        else:
            return (end-start) // 2
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst1 = nums1
        lst2 = nums2
        end1 = len(lst1)
        end2 = len(lst2)
        start1, start2 = 0,0

        while end1 - start1 > 2 and end2 - start2 > 2:
            m1 = self.findMedian(lst1, start1, end1)
            m2 = self.findMedian(lst2, start2, end2)
            cut = min(self.findCut(start1, end1), self.findCut(start2, end2))
            if m1 < m2:
                start1 = start1 + cut
                end2 = end2 - cut
            elif m1 > m2:
                start2 = start2 + cut
                end1 = end1 - cut
            else:
                return m1
        else:
            if (end1 - start1) > (end2 - start2) and (end1 - start1) > 4:
                if (end1 - start1) % 2 == 0:
                    start1 = (end1 - start1) // 2 - 2 + start1
                    end1 = start1 + 4
                else:
                    start1 = (end1 - start1) // 2 - 1 + start1
                    end1 = start1 + 3
            elif (end1 - start1) < (end2 - start2) and (end2 - start2) > 4:
                if (end2 - start2) % 2 == 0:
                    start2 = (end2 - start2) // 2 - 2 + start2
                    end2 = start2 + 4
                else:
                    start2 = (end2 - start2) // 2 - 1 + start2
                    end2 = start2 + 3
              
            lst3 = sorted(lst1[start1: end1] + lst2[start2: end2])
            return self.findMedian(lst3, 0, len(lst3))
        
#### Beats 100% of users' soluton in leetCode####