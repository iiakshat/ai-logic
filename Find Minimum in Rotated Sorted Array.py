# Find Minimum in Rotated Sorted Array

# Problem Statement
# You are given a sorted array of unique integers that has been rotated between 1 and n times.
# For example, [1, 2, 3, 4, 5] might become [3, 4, 5, 1, 2] after two rotations.
# Write a function find_min(nums) that returns the minimum element of the array.
# Your solution must run in O(log n) time.

# Constraints
# 1 <= nums.length <= 5000
# -5000 <= nums[i] <= 5000
# All integers in nums are unique
# nums is sorted and rotated between 1 and n times


def bs(l,h,nums):
    while l<h:
        mid = l+(h-l)//2
        if (nums[mid] > nums[h]): #12345
            l = mid + 1
        else:
            h = mid
    return nums[l]


def find_min(nums):
    l = 0
    h = len(nums) -1
    return bs(l,h,nums)


nums = [3,4,5,1,2]
nums2 = [4,5,6,7,8,1,2,3]
nums3 = [4,5,6,7,8]
print(find_min(nums))
print(find_min(nums2))
print(find_min(nums3))