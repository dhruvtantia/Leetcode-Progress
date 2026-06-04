# Here are my solutions to the Leetcode problems marked Easy
import pandas as pd
import numpy as np

###########################################################
# 1. TwoSum

class Solution(object):
     
    def twoSum(self, nums, target):
            """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
            """
            
            for i in range(len(nums)):
                num1 = nums[i]
                for j in range(i+1, len(nums)):
                    num2 = nums[j]
                    if (num1 + num2 == target): 
                        return [i, j]


###########################################################
# 9. Is Palindrome? 

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        
        string = str(x) 

        if string == string[::-1]:
            return True
        else: return False



###########################################################
# 13. Roman Numeral to integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        curcount = 0
        curindex = 0
        d = {"I": 1, "V": 5, "X": 10,  "L": 50,
                     "C": 100, "D": 500, "M": 1000}

        n = len(s)

        for i in range(n):
            if (i+1) <= n-1 and d[s[i]] < d[s[i+1]]: 
                
                curcount -= d[s[i]]
            else: 
                curcount += d[s[i]]
            
        return curcount

        
###########################################################
# 14. Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def return_common_pre(s1, s2):
            curstring = ""
            # returns the common prefix in s1, s2 if it exists. 
            for i in range(min(len(s1), len(s2))):
                if s1[i] != s2[i]: 
                    return curstring
                else: curstring = curstring + s1[i]
            return curstring
        
        def shortest_str(lst): 
            minlen = 0
            l = list(map(lambda a: len(a) , lst))
            minval = min(l)
            #shortest string returned from list of strings
            for string in lst: 
                if len(string) == minval:
                    return string

        curpre = ""
        
        if ("" in strs) or len(strs) == 0: 
            return ""
        
        elif len(strs) == 1: 
            return strs[0]

        else:
            nlist = []
            for i in strs: 
                nlist.append(i)
            comparer = nlist.pop()
            ans = shortest_str(
                list(map(lambda a: return_common_pre(a, comparer), 
                         strs)))
            return ans


###########################################################
# 28. Index of first occurence of string. 

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        def str_equal(s1, s2): 
            return s1 == s2
        
        n = len(needle) 
        h = len(haystack)

        indices = []

        for i in range(h-n+1):
            if str_equal(needle, haystack[i:i+n]):
                return i 

        return -1


###########################################################
# 26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        def unique(arr):
            lst = []
            for i in range(len(arr)):
                if arr[i] not in lst:
                    lst.append(arr[i])
            return lst
        
        nums[:] = unique(nums)
        k = len(nums)
        return k

###########################################################
# 118. Pascal's Triangle

def fact(n): 
    if n == 0: 
        return 1
    elif n == 1: 
        return 1
    else: 
        return n * fact(n-1)

def nck(n, k):
    numerator = fact(n) 
    denominator = fact(k) * fact(n-k)
    return numerator / denominator 
        
def binom_coefs(x):
    output_list = []
    if x == 0: 
        return [1]
    for i in range(x+1): 
        output_list.append(int(nck(x, i)))
    return output_list
            
def func(numrows): 
    output = []
    for i in range(numrows): 
        output.append(binom_coefs(i))
    return output




###########################################################
# 4. Median of Two Sorted Arrays

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    n1, n2 = len(nums1), len(nums2) 
    i, j = 0, 0

    merged = []

    while i < n1 and j < n2: 
        if nums1[i] < nums2[j]: 
            merged.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]: 
            merged.append(nums2[j])
            j += 1

    # there may be remaining items in 1 or 2
    while i < n1: 
        merged.append(nums1[i])
        i += 1
    while j < n2: 
        merged.append(nums2[j])
        j += 1
    
    median_index = ((len(merged) + 1)//2)


    median = 0

    if len(merged) % 2 == 0: 
        median = (merged[median_index] + merged[median_index - 1])*0.5
    else: 
        median = merged[median_index-1]
    
    return median

#print(findMedianSortedArrays([1, 2], [3]))

###########################################################
# 27. Remove Element

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    newlist = []
    gaps = []
    n = len(nums)
    
    for i in range(n): 
        if val == nums[i]: 
            gaps.append("_")
            n = n - 1
        elif val != nums[i]: 
            newlist.append(nums[i])
    
    newlist.extend(gaps)

    nums[:] = newlist

    return len(newlist) - len(gaps)


###########################################################
# 58. Length of Last Word

def lastword(string): 
    lst = string.split(" ")
    lstt = []

    for i in lst: 
        if i not in (" ", ""):
            lstt.append(i)

    last = lstt[-1]
    return len(last), last, lstt

# print(lastword("Hello World"))
# print(lastword("   fly me   to   the moon  "))
# print(lastword("luffy is still joyboy"))
###########################################################
# 1481. Least Number of Unique Integers after K Removals

def limitOccurrences(nums: list[int], k: int) -> list[int]:
    d = {}
    for number in nums: 
        if number not in d: 
            d[number] = 1
        elif d[number] >= k: 
            d[number] = k
        else: 
            d[number] += 1
    
    unique_list = d.keys()
    result = []

    for key in unique_list: 
        count = d[key]
        while count != 0: 
            result.append(key)
            count -=1
    return result 

###########################################################
# 485. Max Consecutive Ones

def findMaxConsecutiveOnes(nums) -> int:

    strings = list(map(lambda a: str(a), nums))
    strin = ""
    for i in strings: 
        strin = i + strin
    lst = strin.split("0")
    listoflens = list(map(lambda a: len(a), lst))
    return max(listoflens)
#print(findMaxConsecutiveOnes([1,1,0,1,1,1]))

###########################################################
# 283. Move Zeroes

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    newlist = list(filter(lambda a: a != 0, nums))
    zeroes = len(nums) - len(newlist) 
    zeroesl = [0 for i in range(zeroes)]
    newlist.extend(zeroesl)
    nums[:] = newlist
    return nums 

#print(moveZeroes([0,1,0,2,3,5,3]))

###########################################################
# 414. Third Maximum Number

def thirdMax(nums) -> int:
    set1 = set(nums) 
    sortedlist = sorted(set1)
    lst = sorted(list(set1))
    n = len(lst)
    if n < 3: 
        return max(lst) 
    else: 
        return lst[-3]


#print(thirdMax([-1, 2, 3]))

###########################################################
# 867. Transpose Matrix

def transpose(matrix): 
    nrow = len(matrix) 
    ncol = len(matrix[0]) 

    result = []

    for j in range(ncol): 
        row = [] 
        for i in range(nrow): 
            row.append(0)
        result.append(row)

    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = matrix[j][i]
    return result

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))


