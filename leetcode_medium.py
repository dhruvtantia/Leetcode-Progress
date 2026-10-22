# Here are my solutions to the Leetcode problems marked Medium
from typing import List, Optional

###########################################################
# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two sum on the rest of the list, looking for -nums[i]
            seen = set()
            for j in range(i + 1, n):
                needed = -nums[i] - nums[j]
                if needed in seen:
                    triplets.add((nums[i], needed, nums[j]))
                seen.add(nums[j])
        return list(map(lambda t: list(t), triplets))


###########################################################
# 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n):
            first = i + 1
            last = n - 1
            while first < last:
                cursum = nums[i] + nums[first] + nums[last]
                if abs(cursum - target) < abs(closest - target):
                    closest = cursum
                if cursum == target:
                    return cursum
                elif cursum < target:
                    first += 1
                else:
                    last -= 1
        return closest


###########################################################
# 18. 4Sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                # two sum on the rest of the list
                seen = set()
                for k in range(j + 1, n):
                    needed = target - nums[i] - nums[j] - nums[k]
                    if needed in seen:
                        quads.add((nums[i], nums[j], needed, nums[k]))
                    seen.add(nums[k])
        return list(map(lambda t: list(t), quads))


###########################################################
# 19. Remove Nth Node From End of List

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first count the length of the list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # removing the first node
        if n == length:
            return head.next

        # walk to the node just before the one to remove
        cur = head
        for i in range(length - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head


###########################################################
# 22. Generate Parentheses

import itertools

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        # every string of length 2n made of ( and ), keep the valid ones
        allstrings = map(lambda t: "".join(t), itertools.product("()", repeat=2 * n))
        return list(filter(is_valid, allstrings))


###########################################################
# 38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        def say(string):
            result = ""
            count = 1
            for i in range(1, len(string) + 1):
                if i < len(string) and string[i] == string[i - 1]:
                    count += 1
                else:
                    result += str(count) + string[i - 1]
                    count = 1
            return result

        term = "1"
        for i in range(n - 1):
            term = say(term)
        return term


###########################################################
# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def find(start, remaining, current):
            if remaining == 0:
                result.append(current)
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                # i not i+1, because the same number can be reused
                find(i, remaining - candidates[i], current + [candidates[i]])

        find(0, target, [])
        return result


###########################################################
# 43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = "0123456789"
        if num1 == "0" or num2 == "0":
            return "0"

        # multiply like on paper, each digit pair goes into its column
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                result[i + j + 1] += digits.find(num1[i]) * digits.find(num2[j])

        # carry over from right to left
        for k in range(len(result) - 1, 0, -1):
            result[k - 1] += result[k] // 10
            result[k] = result[k] % 10

        answer = "".join(map(lambda d: digits[d], result))
        return answer.lstrip("0")


###########################################################
# 46. Permutations

import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(lambda t: list(t), itertools.permutations(nums)))


###########################################################
# 47. Permutations II

import itertools

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique = set(itertools.permutations(nums))
        return list(map(lambda t: list(t), unique))


###########################################################
# 50. Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0
        n = abs(n)
        result = 1
        # square x and halve n each step
        while n > 0:
            if n % 2 == 1:
                result = result * x
            x = x * x
            n = n // 2
        if negative:
            return 1 / result
        return result


###########################################################
# 24. Swap Nodes in Pairs

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            # swap the pair by rewiring the links
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return dummy.next


###########################################################
# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))  # anagrams share the same sorted letters
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())


###########################################################
# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result


###########################################################
# 2. Add Two Numbers

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            tail.next = ListNode(total % 10)
            tail = tail.next
            carry = total // 10
        return dummy.next


###########################################################
# 6. Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        row = 0
        step = 1
        # walk down the rows, then back up, dropping one letter in each row
        for ch in s:
            rows[row] += ch
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return "".join(rows)


###########################################################
# 11. Container With Most Water

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0
        while left < right:
            width = right - left
            best = max(best, width * min(height[left], height[right]))
            # move the shorter wall inward, it can't do better staying put
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best


