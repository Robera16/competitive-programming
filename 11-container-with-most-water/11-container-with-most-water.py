class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointer=0
        rightPointer=len(height)-1
        n=len(height)/2
        area=calculateArea(leftPointer, rightPointer, height)
        
        while(leftPointer < rightPointer):
            area=max(area, calculateArea(leftPointer, rightPointer, height))
            if height[leftPointer] < height[rightPointer]:
                leftPointer+=1
                        
            elif height[rightPointer] < height[leftPointer]:
                rightPointer-=1
            else:
                leftPointer+=1
        return area

def calculateArea(leftPointer, rightPointer, height):
    width = rightPointer - leftPointer
    height = min(height[leftPointer], height[rightPointer])  
    area = width * height
    return area