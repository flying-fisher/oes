'''Python exercise1: Search for a Range (from leetcode.com)
Problem description:

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]. 
'''
nums_str = input('Input nums:').split(',')
nums = []
for i in nums_str:
    nums.append(float(i))
target = float(input('Input target:'))
def a(target,id,list):
    left,right = id,id
    while left > 0 and list[left-1] == target:
        left -= 1
    while right < len(list) - 1 and list[right+1] == target:
        right += 1
    return [left,right]
            
def search(target,list):
    left = 0
    right = len(list) - 1
    if target < list[left] or target > list[right]:
        return [-1,-1]
            
    while left <= right:
        mid = int((left + right) / 2)
        if target == list[mid]:
            return a(target,mid,list)
        elif target < list[mid]:
            right = mid - 1   
        else:
            left = mid + 1
    return [-1,-1]
if nums == []:
    print('-1 -> -1')
a = search(target,nums)
print('%d -> %d'%(a[0],a[1]))