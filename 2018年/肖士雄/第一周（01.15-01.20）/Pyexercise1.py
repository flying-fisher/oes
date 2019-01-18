'''Python exercise1: Container With Most Water (from leetcode.com)
Problem description:

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2. 
'''
import os
class Solution(object):
    def min(self,x,y):
        if x <= y:
            return x
        else:
            return y
    def maxArea(self, height):
        count = len(height)
        i,j = 0, count-1
        max = min(height[i],height[j])*(j-i)
        print()
        while i < j:
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            if min(height[i],height[j])*(j-i) > max:
                max = min(height[i],height[j])*(j-i)
        return max
    
a = input("Please input the sequence: ").split()
height = []
for i in range(len(a)):
    height.append(int(a[i]))
result = Solution()
print("The most volume is %s. " %(result.maxArea(height)))
os.system("pause")