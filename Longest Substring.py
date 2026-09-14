#  Longest Substring Without Repeating Characters

# Problem Statement
# Given a string s, find the length of the longest substring that contains no repeating characters.
# A substring is a contiguous sequence of characters within the string.

# Constraints
# 0 <= s.length <= 5 x 10^4
# s consists of English letters, digits, symbols, and spaces
# Expected time complexity: O(n)


# Input:  s = "abcabcbb"
# Output: 3   (substring "abc")
 
# Input:  s = "bbbbb"
# Output: 1   (substring "b")


def longest_substring(s):
    maxx = 0
    i,j = 0,0
    seen = {}
    ans = [i,j]
    for j, x in enumerate(s):
        if x in seen and seen[x] >= i:
            i = seen[x] + 1
        
        seen[x] = j
        if maxx< j-i+1:
            maxx = j-i+1
            ans = [i,j]
    
    return s[ans[0]: ans[1]+1]      
        
        
print(longest_substring("abcabcbb"))
print(longest_substring("bbbbbb"))