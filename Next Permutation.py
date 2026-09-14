# Coding Q3 - Next Permutation

# Problem Statement
# Given an array of integers nums, rearrange it into the next lexicographically greater permutation of its elements.
# If no such arrangement is possible (the array is in descending order), rearrange it into the smallest possible order (sorted ascending).
# The replacement must be done in-place using only constant extra memory.
# Do NOT use any built-in permutation functions.

# Constraints
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# Must be solved in-place with O(1) extra space

# Open Test Cases (Visible to Candidate)
# Input:  nums = [1, 2, 3]
# Output: [1, 3, 2]
 
# Input:  nums = [3, 2, 1]
# Output: [1, 2, 3]

# 123
# 132
# 213
# 231
# 312
# 321

# 1234
# 1324
# 1432


def reverse_(nums,n):
    l,r = 0,n-1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1
    return nums
    
def next_permutation(nums):
    n = len(nums)
    if n==1: return nums
    if n==2: return [nums[1], nums[0]]
    if nums[0] > nums[1] and nums[0] > nums[-1]:
        return reverse_(nums,n)
    
    nums[1],nums[2] = nums[2],nums[1]
    return nums

print(next_permutation([1,2,3,4]))
print(next_permutation([1,2,3]))
print(next_permutation([3,2,1]))