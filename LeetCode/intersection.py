class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        array_intersection = []
        if len(set1) < len(set2):
            for x in set1:
                if x in set2:
                    array_intersection.append(x)
        else:
            for x in set2:
                if x in set1:
                    array_intersection.append(x)
        return array_intersection
        