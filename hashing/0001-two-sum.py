"""
Problem   : Two Sum (https://leetcode.com/problems/two-sum/)
Topic     : Hashing
Difficulty: Easy
Approach  : Walk the array once. For each number, check whether its complement
            (target - num) was already seen; if so, return both indices.
            Otherwise store num -> index in a hash map.
Time      : O(n)
Space     : O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    print("All tests passed!")
