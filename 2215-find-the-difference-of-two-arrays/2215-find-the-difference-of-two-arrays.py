class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = list(set(nums1)), list(set(nums2))
        nums1.sort()
        nums2.sort()
        answer1, answer2 = set(), set()
        pt1, pt2 = 0, 0
        while pt1 < len(nums1) and pt2 < len(nums2):
            if nums1[pt1] < nums2[pt2]:
                answer1.add(nums1[pt1])
                pt1+=1
                
            elif nums1[pt1] > nums2[pt2]:
                answer2.add(nums2[pt2])
                pt2+=1
            else:
                pt1+=1
                pt2+=1
          
        answer1 = list(answer1)
        answer2 = list(answer2)
        if pt1 < len(nums1):
            answer1.extend(nums1[pt1:])
            
        if pt2 < len(nums2):
            answer2.extend(nums2[pt2:])
        
        return [answer1, answer2]