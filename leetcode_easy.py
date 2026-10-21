# Here are my solutions to the Leetcode problems marked Easy
import pandas as pd
import numpy as np

###########################################################
# 1. Two Sum

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
# 9. Palindrome Number

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
# 13. Roman to Integer

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
# 28. Find the Index of the First Occurrence in a String

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
# 58. Length of Last Word

def lastword(string): 
    lst = string.split(" ")
    lstt = []

    for i in lst: 
        if i not in (" ", ""):
            lstt.append(i)

    last = lstt[-1]
    return len(last), last, lstt


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

#print(transpose([[1,2,3],[4,5,6],[7,8,9]]))


###########################################################
# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2) 
        nums1.sort()
        n = len(nums1)
        i = (n-1) //2 
        if n % 2 == 0: 
            return 0.5*(nums1[i] + nums1[i+1])
        else: 
            return nums1[i]


###########################################################
# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: 
            sign = -1
        else: sign = 1

        x = abs(x) 
        number = sign * int(str(x)[::-1])
        if number < (-2)**31 or number > (2)**31 - 1: 
            return 0
        else: return number


###########################################################
# 3940. Limit Occurrences in Sorted Array

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
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
# 3931. Check Adjacent Digit Differences

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        lst = list(s)
        listofint = list(map(lambda a: int(a), lst))
        n = len(s)
        listofdiff = []
        for i in range(n-1):
            listofdiff.append(abs(listofint[i+1]-listofint[i]))

        for diff in listofdiff:
            if diff>2:
                return False
        return True


###########################################################
# 3925. Concatenate Array With Reverse

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = nums[:]
        n = len(nums) 

        while n > 0: 
            ans.append(nums[n-1])
            n = n - 1
        return ans


###########################################################
# 3908. Valid Digit Number

class Solution:
    def validDigit(self, k: int, x: int) -> bool:
        n = str(k)
        x = str(x) 
        if not n: 
            return False
        if (n[0] != x) and (x in list(n[1:])):
            return True
        
        return False


###########################################################
# 3870. Count Commas in Range

class Solution:
    def countCommas(self, n: int) -> int:
        def count_commas(int):
            k=len(str(int))
            if k<=3: return 0
            if k % 3==0: return (k//3 - 1)
            return (k//3)
        
        listofints = range(1, n+1)
        comma_count = list(map(count_commas, listofints))
        return sum(comma_count)


###########################################################
# 3866. First Unique Even Element

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        liste = list(filter(lambda a: a%2==0, nums))
        d = {}
        for number in liste: 
            if number not in d:
                d[number] = 1
            else: 
                d[number] += 1
        
        for number in liste: 
            if d[number] == 1: 
                return number
        return -1


###########################################################
# 3718. Smallest Missing Multiple of K

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        counter = 1

        while counter * k in nums: 
            counter += 1
        return counter * k


###########################################################
# 3707. Equal Score Substrings

class Solution:
    def scoreBalance(self, s: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)): 
            fscore = 0
            scoree = 0
            first = s[:i]
            second = s[i:]

            for char in first: 
                fscore += (letters.find(char) + 1)

            for letter in second: 
                scoree += (letters.find(letter) + 1)
            if fscore == scoree: return True

        return False


###########################################################
# 3663. Find the Least Frequent Digit

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        listofstr = list(str(n))

        d = {}

        for string in listofstr: 
            if string not in d: 
                d[string] = 1
            else: 
                d[string] += 1

        minfreq = min(d.values())
        minfreqlst = []

        for key in d: 
            if d[key] == minfreq: 
                minfreqlst.append(int(key))
        return min(minfreqlst)


###########################################################
# 3658. GCD of Odd and Even Sums

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odds = n * n
        evens = n * (n + 1)
        a = evens
        b = odds
        remainder = n

        while remainder != 0:
            remainder = a%b
            a = b
            b = remainder
        return a


###########################################################
# 3622. Check Divisibility by Digit Sum and Product

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = list(map(lambda a: int(a), list(str(n))))
        sumd = sum(digits) 
        prod = 1
        for digit in digits:
            prod *= digit
        divisor = sumd + prod

        return (n % divisor == 0)


###########################################################
# 3550. Smallest Index With Digit Sum Equal to Index

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        def sum_digits(number):
            cursum = 0
            for i in str(number): 
                cursum = cursum + int(i)
            return cursum
        
        for i in range(len(nums)): 
            digsum = sum_digits(nums[i])
            if digsum == i: 
                return i
        
        return -1


###########################################################
# 2879. Display the First Three Rows

import pandas as pd
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employees, columns = ["employee_id", "name", "department", "salary"])
    return employees[0:3]


###########################################################
# 2404. Most Frequent Even Element

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        evenlist = list(filter(lambda a: a % 2 == 0, nums))

        if not evenlist: 
            return -1
        
        d = {}

        for item in evenlist: 
            if item not in d: 
                d[item] = 0
            else: 
                d[item] += 1

        freq = d.values()
        mostoccuring = max(freq)
        lst = []

        for key in d: 
            if d[key] == mostoccuring: 
                lst.append(key)
        return min(lst)


###########################################################
# 1929. Concatenation of Array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        ans.extend(nums) 
        return ans


###########################################################
# 1002. Find Common Characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        def dcreator(string):
            d = {}
            for s in string: 
                if s not in d: 
                    d[s] = 1
                else: d[s] += 1
            return d
        
        listofdict = []
        for word in words: 
            listofdict.append(dcreator(word))
        
        compdict = listofdict[0]
        commons = {}

        for ckey in compdict: 
            allothercounts = []
            for dictionary in listofdict: 
                if ckey in dictionary: 
                    allothercounts.append(dictionary[ckey])
                else: 
                    allothercounts.append(0)
            
            if 0 not in allothercounts:
                commons[ckey] = min(allothercounts)
        
        result = []

        for key in commons:
            times = commons[key]
            while times > 0:
                times = times - 1
                result.append(key)
        return result  


###########################################################
# 961. N-Repeated Element in Size 2N Array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        set1 = set() 
        for number in nums: 
            if number not in set1: 
                set1.add(number)
            else: return number


###########################################################
# 917. Reverse Only Letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        fixed_indices = []
        onlyletters = ""
        for i in range(len(s)):
            if s[i] not in letters:
                fixed_indices.append((i, s[i]))
            else: 
                onlyletters += s[i] 
        revletters = onlyletters[::-1]

        for i in range(len(fixed_indices)):
            # check the first entry in the tuple, thats the index of insertion
            # then divide the main string, which is rev letters and add the 
            # second entry in the tuple into the string. 
            tup = fixed_indices[i]
            first = revletters[:tup[0]]
            last = revletters[tup[0]:]
            revletters = first + tup[1] + last
        
        return revletters


###########################################################
# 896. Monotonic Array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def moninc(lst): 
            for i in range(len(lst)-1): 
                if lst[i] > lst[i+1]: 
                    return False
            return True
        
        def mondec(lst):
            for i in range(len(lst)-1): 
                if lst[i] < lst[i+1]:
                    return False
            return True
        
        return (mondec(nums) or moninc(nums))


###########################################################
# 860. Lemonade Change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_bills = 0
        ten_dollar_bills = 0
        for customer_bill in bills:
            if customer_bill == 5:
                five_dollar_bills += 1
            elif customer_bill == 10:
                if five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
                else:
                    return False
            else:  
                if ten_dollar_bills > 0 and five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills -= 1
                elif five_dollar_bills >= 3:
                    five_dollar_bills -= 3
                else:
                    return False
        return True


###########################################################
# 819. Most Common Word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Convert to lowercase first to standardize everything
        paragraph = paragraph.lower()
        
        clean_paragraph = ""
        for char in paragraph:
            if char.isalnum():
                clean_paragraph += char
            else:
                clean_paragraph += " "
        
        listofstrings = clean_paragraph.split()
        
        finalstrings = []
        for string in listofstrings:
            if string not in banned and string != "":
                finalstrings.append(string)
                
        d = {}
        for string in finalstrings:
            if string in d:
                d[string] += 1
            else:
                d[string] = 1
                
        maxval = max(d.values())
        for key in d:
            if d[key] == maxval:
                return key


###########################################################
# 806. Number of Lines To Write String

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        linecount = 1
        currentwidth = 0
        wlimit = 100
        letters = "abcdefghijklmnopqrstuvwxyz"

        # mapping the widths to the letters 
        d = {}
        for i in range(len(letters)):
            d[letters[i]] = widths[i]
        
        for char in s:
            currentwidth = currentwidth + d[char] 
            if currentwidth > wlimit: 
                linecount += 1
                currentwidth = d[char]
            
        if currentwidth > 100: 
            currentwidth -= 100 
            linecount += 1

        result = [linecount, currentwidth]
        return result


###########################################################
# 804. Unique Morse Code Words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse = [".-","-...","-.-.","-..",".","..-.",
                "--.","....","..",".---","-.-",".-..",
                "--","-.","---",".--.","--.-",".-.",
                "...","-","..-","...-",".--","-..-",
                "-.--","--.."]

        letters = "abcdefghijklmnopqrstuvwxyz"

        transformed = []

        for word in words:
            code = ""
            for letter in word: 
                code += morse[letters.find(letter)]
            transformed.append(code)
        
        unique = set(transformed)
        return len(unique)


###########################################################
# 744. Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        chars = "abcdefghijklmnopqrstuvwxyz"
        n = len(letters) 
        targ = chars.find(target)
        for i in range(n): 
            strindex = chars.find(letters[i])
            if strindex > targ: 
                return letters[i]
        return letters[0]


###########################################################
# 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums) 
        for i in range(n): 
            if sum(nums[:i]) == sum(nums[i+1:]): 
                return i
        return -1


###########################################################
# 704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        while first <= last: 
            midpoint = (first + last) // 2
            mid = nums[midpoint]
            if target == mid: 
                return midpoint 
            elif target < mid:
                last = midpoint - 1
            elif target > mid: 
                first = midpoint + 1
        return -1 


###########################################################
# 674. Longest Continuous Increasing Subsequence

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxlen = 1
        curlen = 1
        n = len(nums) 

        for i in range(n-1): 
            if nums[i] < nums[i+1]: 
                curlen += 1
            elif curlen > maxlen: 
                maxlen = curlen
                curlen = 1
            else:
                curlen = 1

        if curlen > maxlen: 
            maxlen = curlen
        
        return maxlen 


###########################################################
# 645. Set Mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        idealsum = (n*(n+1))//2
        set1 = set(nums) 
        setl = len(set1)
        sumwithoutmissing = sum(set1)
        missing = idealsum - sumwithoutmissing
        repeated = sum(nums) - sum(set1) 
        return [repeated, missing]


###########################################################
# 628. Maximum Product of Three Numbers

# either itll be the product of the last three positives in a sorted list
# or the first two negative items multiplied by the biggest positive item 
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3]) 


###########################################################
# 599. Minimum Index Sum of Two Lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1, set2 = set(list1), set(list2) 
        commons = list(set1.intersection(set2))
        d = {}

        for string in commons: 
            ind1, ind2 = list1.index(string), list2.index(string)
            summ = ind1 + ind2
            d[string] = summ
        
        minind = min(d.values())
        result = []
        for key in d: 
            if d[key] == minind: 
                result.append(key)

        return result 


###########################################################
# 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        output = range(1, len(score)+1)
        sortedl = sorted(score, reverse = True)
        relativeindices = []
        for i in score: 
            index = sortedl.index(i)
            relativeindices.append(index)
        
        for i in range(len(relativeindices)): 
            if relativeindices[i] == 0: 
                relativeindices[i] = "Gold Medal"
            elif relativeindices[i] == 1: 
                relativeindices[i] = "Silver Medal"
            elif relativeindices[i] == 2: 
                relativeindices[i] = "Bronze Medal"
            else: 
                relativeindices[i] = str(relativeindices[i] + 1)
        return relativeindices


###########################################################
# 500. Keyboard Row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "QWERTYUIOPqwertyuiop"
        second = "ASDFGHJKLasdfghjkl"
        third = "ZXCVBNMzxcvbnm"

        def is_subset(s1, bigstring): 
            smallset = set(list(s1))
            bigset = set(list(bigstring))
            return smallset.intersection(bigset) == smallset
        
        def subsetofrow(string): 
            one = is_subset(string, first)
            two = is_subset(string, second)
            three = is_subset(string, third)
            return one or two or three

        result = list(filter(subsetofrow, words))
        return result 


###########################################################
# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        numbers = set(nums)
        ideal = range(1, n+1)
        for number in ideal:
            if number not in numbers: 
                result.append(number)
        return result


###########################################################
# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ds = {}
        dt = {}

        for char in s: 
            if char not in ds: 
                ds[char] = 1
            else: ds[char] += 1

        for char in t: 
            if char not in dt: 
                dt[char] = 1
            else: dt[char] += 1

        for key in dt: 
            if key not in ds or ds[key] != dt[key]: 
                return key


###########################################################
# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s: 
            if char not in d:
                d[char] = 1
            else: d[char] += 1
        
        for i in range(len(s)): 
            if d[s[i]] == 1: 
                return i 
        return -1 


###########################################################
# 367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num ** 0.5) == num ** 0.5


###########################################################
# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        n = len(nums1)
        iterable = nums2[:]
        for i in range(n): 
            if nums1[i] in iterable: 
                result.append(nums1[i])
                iterable.remove(nums1[i])
        return result 


###########################################################
# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))


###########################################################
# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actualsum = sum(nums) 
        n = len(nums) + 1
        theorsum = n*(n-1)*0.5
        return int(theorsum - actualsum)


###########################################################
# 258. Add Digits

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def digits_num(integer): 
            return len(list(str(integer)))
        
        def add_digits(number): 
            return sum(list(map(lambda a: int(a), list(str(number)))))

        def onedigit(number):
            if digits_num(number) == 1: 
                return True
        
        cursum = add_digits(num)

        while not onedigit(cursum): 
            cursum = add_digits(cursum)

        if onedigit(cursum): 
            return cursum


###########################################################
# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


###########################################################
# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 1: 
            return True
        if n < 1: 
            return False
        else: 
            return self.isPowerOfTwo(n / 2)


###########################################################
# 219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def less_than_k(list_of_indices):
            n = len(list_of_indices)
            listofdiffs = []
            for i in range(n-1):
                listofdiffs.append(abs(list_of_indices[i+1] - list_of_indices[i]))
            final_list = list(filter(lambda a: a<=k, listofdiffs))
            if not final_list: 
                return False
            else: return True

        # dictionary with key as num and val as list of indices

        d = {}

        for i in range(len(nums)): 
            if nums[i] not in d: 
                d[nums[i]] = [i]
            else: 
                d[nums[i]].append(i)
        
        # filter the elements in the dictionary that have at least 2 instances
        indices_lol = d.values()
        repeated_indices_list = list(filter(lambda l: len(l)>1, indices_lol))

        # create a function that inputs a list and returns true if the difference 
        # between two consecutive indices is less than equal to k. len(list)>1

        # map this function on the list of repeated indices as its a list of lists, check if 
        # the output has a True, then True, else false

        result = (True in list(map(less_than_k, repeated_indices_list)))

        return result


###########################################################
# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for number in nums: 
            if number not in d: 
                d[number] = 1
            else: 
                return True
        return False


###########################################################
# 169. Majority Element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        d = {}

        for number in nums: 
            if number not in d: 
                d[number] = 1
            else: 
                d[number] += 1
        vals = d.values()
        mode = max(vals) 

        for key in d: 
            if d[key] == mode: 
                return key


###########################################################
# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for number in nums: 
            if number not in d:
                d[number] = 1
            else: d[number] += 1
        for key in d: 
            if d[key] == 1: 
                return key


###########################################################
# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def factorial(n): 
            if n in [0,1]: 
                return 1
            else: 
                return n *factorial(n-1) 
        
        def combination(n, k): 
            return (factorial(n))//((factorial(n-k)*factorial(k)))
        
        result = []
        for i in range(rowIndex+1):
            result.append(combination(rowIndex, i))
        return result 


###########################################################
# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = []

        lst1 = nums1[:m]

        lst2 = nums2[:]

        i, j = 0, 0

        while i < m and j < n: 
            if lst1[i] > lst2[j]: 
                merged.append(lst2[j])
                j = j + 1
            else: 
                merged.append(lst1[i])
                i += 1

        if i == len(lst1):
            merged.extend(lst2[j:])
        if j == n: 
            merged.extend(lst1[i:])
        
        nums1[:] = merged


###########################################################
# 81. Search in Rotated Sorted Array II

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return (target in nums)


###########################################################
# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) in [0, 1]: 
            return nums

        def dcreator(lst): 
            d = {}
            for number in lst: 
                if number not in d: 
                    d[number] = 1
                else: d[number] += 1
            return d
        result = []

        d = dcreator(nums)

        for i in range(3): 
            counti = d.get(i, 0)
            while counti != 0:
                result.append(i)
                counti -= 1
        nums[:] = result

        return nums


###########################################################
# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i ** 2 <= x: 
            i += 1
        return i - 1


###########################################################
# 66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringnum = list(map(lambda a: str(a), digits))
        strr = ""
        for char in stringnum: 
            strr += char
        integer = int(strr)
        increment1 = 1 + integer
        listofstring = list(str(increment1))
        return list(map(lambda a: int(a), listofstring))


###########################################################
# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        s = s.strip()
        string = ""
        for char in s:
            if char.isalnum():
                string += char

        last = len(string) - 1

        while first < last:
            if not string[first].isalnum():
                first += 1
            elif not string[first].isalnum():
                last -= 1
            elif string[first].lower() == string[last].lower():
                first += 1
                last -= 1
            else:
                return False

        return True

###########################################################
# 344. Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

###########################################################
# 8. String to Integer (atoi)

# Placeholder for the corresponding solution block.

###########################################################
# 342. Power of Four

import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        logn = math.log(n)
        ln4 = math.log(4)
        if int(logn / ln4) == (logn / ln4):
            return True
        else:
            return False

###########################################################
# 326. Power of Three


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n / 3
        return n == 1

###########################################################
# 392. Is Subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indices = []
        findin = t

        for i in range(len(s)):
            index = findin.find(s[i])

            if index == -1:
                return False

            indices.append(index)
            findin = findin[index + 1:]

        return True

###########################################################
# 263. Ugly Number


class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        isdivisible = True

        while isdivisible:

            if n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                isdivisible = False
        return n == 1

###########################################################
# 202. Happy Number


class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)

        def sumdigs(string):
            listofdigs = list(string)
            cursum = 0
            for digit in listofdigs:
                cursum += int(digit) ** 2
            return str(cursum)

        sums = set()
        cursum = sumdigs(n)

        if cursum == "1":
            return True

        while cursum not in sums:
            if cursum == "1":
                return True
            sums.add(cursum)
            cursum = sumdigs(cursum)

        return False

###########################################################
# 345. Reverse Vowels of a String


class Solution:
    def reverseVowels(self, s: str) -> str:
        vindices = []
        vpres = []
        vowels = "aeiouAEIOU"
        for i in range(len(s)):
            if s[i] in vowels:
                vpres.append(s[i])
                vindices.append(i)

        vpres = vpres[::-1]
        slist = list(s)
        for i in range(len(vindices)):
            slist[vindices[i]] = vpres[i]

        return "".join(slist)

###########################################################
# 1502. Can Make Arithmetic Progression From Sequence


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        diffs = set()
        arr.sort()
        for i in range(n - 1):
            diffs.add(arr[i] - arr[i + 1])
        return len(diffs) == 1

###########################################################
# 2485. Find Pivot Integer


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) * 0.5

        if n <= 0:
            return -1
        if n == 1:
            return 1

        for i in range(1, n + 1):
            backsum = i * (i + 1) * 0.5
            aftersum = total - backsum + i
            if aftersum == backsum:
                return i
        return -1

###########################################################
# 728. Self Dividing Numbers


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def verifier(num):
            digits = list(str(num))
            if "0" in digits:
                return False
            for digit in digits:
                digint = int(digit)
                if num % digint != 0:
                    return False
            return True

        rangee = range(left, right + 1)
        lst = list(filter(verifier, rangee))

        return lst

###########################################################
# 1015. Smallest Integer Divisible by K

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        rem = 0
        for i in range(k):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return i + 1
        return -1

###########################################################
# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack


###########################################################
# 21. Merge Two Sorted Lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next


###########################################################
# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


###########################################################
# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(result))


###########################################################
# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(n - 1):
            one, two = one + two, one
        return one


###########################################################
# 83. Remove Duplicates from Sorted List

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


###########################################################
# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            min_price = min(min_price, price)
            best = max(best, price - min_price)
        return best


###########################################################
# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for a, b in zip(s, t):
            if s_to_t.get(a, b) != b or t_to_s.get(b, a) != a:
                return False
            s_to_t[a] = b
            t_to_s[b] = a
        return True


###########################################################
# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        p_to_w = {}
        w_to_p = {}
        for p, w in zip(pattern, words):
            if p_to_w.get(p, w) != w or w_to_p.get(w, p) != p:
                return False
            p_to_w[p] = w
            w_to_p[w] = p
        return True


###########################################################
# 94. Binary Tree Inorder Traversal

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result


###########################################################
# 100. Same Tree

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


###########################################################
# 101. Symmetric Tree

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            # outside pair and inside pair must both match
            return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)

        return mirror(root.left, root.right)


###########################################################
# 104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


###########################################################
# 110. Balanced Binary Tree

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


###########################################################
# 111. Minimum Depth of Binary Tree

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # if one side is missing, the path has to go down the other side
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


###########################################################
# 112. Path Sum

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        remaining = targetSum - root.val
        # a leaf node
        if not root.left and not root.right:
            return remaining == 0
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


###########################################################
# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = 0
        for char in columnTitle:
            number = number * 26 + (letters.find(char) + 1)
        return number


###########################################################
# 206. Reverse Linked List

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode
        return prev


###########################################################
# 108. Convert Sorted Array to Binary Search Tree

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # middle element becomes the root so both sides are balanced
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


###########################################################
# 141. Linked List Cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False


###########################################################
# 144. Binary Tree Preorder Traversal

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def preorder(node):
            if not node:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return result


###########################################################
# 145. Binary Tree Postorder Traversal

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

        postorder(root)
        return result


###########################################################
# 160. Intersection of Two Linked Lists

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_in_a = set()
        cur = headA
        while cur:
            nodes_in_a.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in nodes_in_a:
                return cur
            cur = cur.next
        return None


###########################################################
# 168. Excel Sheet Column Title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = ""
        while columnNumber > 0:
            # subtract 1 because A is 1 not 0
            columnNumber -= 1
            title = letters[columnNumber % 26] + title
            columnNumber = columnNumber // 26
        return title


###########################################################
# 190. Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        bits = format(n, "032b")
        return int(bits[::-1], 2)


###########################################################
# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


###########################################################
# 203. Remove Linked List Elements

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


###########################################################
# 225. Implement Stack using Queues

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        # add to the back, then move everything in front of it behind it
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


###########################################################
# 226. Invert Binary Tree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # swap the children, then invert each side
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


###########################################################
# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            # keep going while the next number is one more
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))
            i += 1
        return result


###########################################################
# 232. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        self.instack.append(x)

    def move(self):
        # only refill the out stack when it is empty, this reverses the order
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

    def pop(self) -> int:
        self.move()
        return self.outstack.pop()

    def peek(self) -> int:
        self.move()
        return self.outstack[-1]

    def empty(self) -> bool:
        return not self.instack and not self.outstack


###########################################################
# 234. Palindrome Linked List

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values == values[::-1]


###########################################################
# 257. Binary Tree Paths

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def walk(node, path):
            if not node:
                return
            path = path + str(node.val)
            # a leaf node, the path is complete
            if not node.left and not node.right:
                result.append(path)
                return
            walk(node.left, path + "->")
            walk(node.right, path + "->")

        walk(root, "")
        return result


###########################################################
# 278. First Bad Version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n
        while first < last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1
        return first


###########################################################
# 292. Nim Game

class Solution:
    def canWinNim(self, n: int) -> bool:
        # if n is a multiple of 4 the opponent can always leave a multiple of 4
        return n % 4 != 0


###########################################################
# 303. Range Sum Query - Immutable

class NumArray:

    def __init__(self, nums: List[int]):
        # prefix[i] is the sum of the first i numbers
        self.prefix = [0]
        for number in nums:
            self.prefix.append(self.prefix[-1] + number)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


###########################################################
# 338. Counting Bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            # i // 2 is i without its last bit, i % 2 is the last bit
            bits[i] = bits[i // 2] + i % 2
        return bits


###########################################################
# 374. Guess Number Higher or Lower

class Solution:
    def guessNumber(self, n: int) -> int:
        first = 1
        last = n
        while first <= last:
            mid = (first + last) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                last = mid - 1
            else:
                first = mid + 1
        return -1


###########################################################
# 412. Fizz Buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer


###########################################################
# 461. Hamming Distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # xor has a 1 wherever the bits of x and y are different
        diff = x ^ y
        count = 0
        while diff > 0:
            count += diff % 2
            diff = diff // 2
        return count


###########################################################
# 938. Range Sum of BST

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        total = 0
        if low <= root.val <= high:
            total += root.val
        return total + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


###########################################################
# 942. DI String Match

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        result = []
        # for I use the smallest number left, for D use the biggest
        for char in s:
            if char == "I":
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)
        return result


###########################################################
# 944. Delete Columns to Make Sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for j in range(len(strs[0])):
            column = []
            for word in strs:
                column.append(word[j])
            if column != sorted(column):
                count += 1
        return count


###########################################################
# 1021. Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        depth = 0
        for char in s:
            if char == "(":
                # only keep it if it is not the outer opening bracket
                if depth > 0:
                    result += char
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result += char
        return result


###########################################################
# 1022. Sum of Root To Leaf Binary Numbers

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def walk(node, current):
            if not node:
                return 0
            # shift left by one bit and add this node's bit
            current = current * 2 + node.val
            if not node.left and not node.right:
                return current
            return walk(node.left, current) + walk(node.right, current)

        return walk(root, 0)


###########################################################
# 1051. Height Checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count


###########################################################
# 1108. Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


###########################################################
# 1122. Relative Sort Array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for number in arr1:
            if number not in d:
                d[number] = 1
            else:
                d[number] += 1

        result = []
        # first the numbers in arr2's order
        for number in arr2:
            result.extend([number] * d[number])
            d[number] = 0

        # then whatever is left, in sorted order
        leftovers = []
        for number in d:
            leftovers.extend([number] * d[number])
        result.extend(sorted(leftovers))
        return result


###########################################################
# 463. Island Perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    perimeter += 4
                    # a shared edge with the cell above or to the left hides 2 sides
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
        return perimeter


###########################################################
# 476. Number Complement

class Solution:
    def findComplement(self, num: int) -> int:
        # find the first power of two above num; one less than it is all 1s
        power = 1
        while power <= num:
            power *= 2
        return (power - 1) - num


###########################################################
# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for x in nums1:
            start = nums2.index(x)
            answer = -1
            for j in range(start + 1, len(nums2)):
                if nums2[j] > x:
                    answer = nums2[j]
                    break
            result.append(answer)
        return result


###########################################################
# 509. Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


###########################################################
# 557. Reverse Words in a String III

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        return " ".join(word[::-1] for word in words)


###########################################################
# 561. Array Partition

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # after sorting, pair neighbours; the smaller of each pair is every other number
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total


###########################################################
# 575. Distribute Candies

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # she can eat n/2 candies, but never more kinds than exist
        return min(len(set(candyType)), len(candyType) // 2)


###########################################################
# 15. 3Sum (work in progress)

import itertools

def threeSum(nums: list[int]) -> list[list[int]]:
    def sumlinds(linds, listt):
        sum = 0 
        for index in linds: 
            sum += listt[index]
        return sum == 0
    
    def number(lst):
        listt = []
        for index in lst:
            listt.append(nums[index])
        return listt

    indiceslist = range(0, len(nums))
    listoflists = list(itertools.combinations(indiceslist, 3))
    
    listofvalidinds = list(filter(lambda l: sumlinds(l, nums), listoflists))

    listofgroups = list(map(number, listofvalidinds))
    listt = list(map(lambda l: tuple(l), listofgroups))
    newlist = []

    for items in listt: 
        newlist.append(sorted(list(items)))

    newset = set(newlist)

    return newset

lst = threeSum([-1,0,1,2,-1,-4])
print(lst)


