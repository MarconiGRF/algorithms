from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        answ = []

        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums1.append(nums1[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1

        if i < m:
            while i < m:
                nums1.append(nums1[i])
                i += 1
        if j < n:
            while j < n:
                nums1.append(nums2[j])
                j += 1

        nums1 = answ