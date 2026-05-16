class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = m
        self.n = n
        index = 0
        for i in range(self.m, len(self.nums1)):
            self.nums1[i] = self.nums2[index]
            index += 1
        
        return self.nums1.sort()
        