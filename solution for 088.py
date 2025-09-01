class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        
class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        point1, point2 = 0, 0
        while point1 < m or point2 < n:
            if point1 == m:
                sorted.append(nums2[point2])
                point2 +=1
            elif point2 == n:
                sorted.append(nums1[point1])
                point1 +=1
            elif nums1[point1] < nums2[point2]:
                sorted.append(nums1[point1])
                point1 +=1
            else:
                sorted.append(nums2[point2])
                point2 +=1
        nums1[:] = sorted


            

        