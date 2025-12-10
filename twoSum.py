"""
Author: Mohamed Malek Loucif
Date: 2025-12-05
Lab: Section D
Description: Implements four versions of the classic Two Sum problem:
"""

from typing import List, Tuple


def twoSumLoops(nums: List[int], target: int) -> Tuple[int, int] | None:
   
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return i, j
    return None


def twoSumDict(nums: List[int], target: int) -> Tuple[int, int] | None:
   
    seen: dict[int, int] = {}
    for j, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            i = seen[complement]
            return i, j
        seen[value] = j
    return None


def twoSumLoopsAll(nums: List[int], target: int) -> List[List[int]]:
    
    n = len(nums)
    result: List[List[int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                result.append([i, j])
    return result


def twoSumDictAll(nums: List[int], target: int) -> List[List[int]]:
   
    result: List[List[int]] = []
    seen_indices: dict[int, List[int]] = {}

    for j, value in enumerate(nums):
        complement = target - value
        if complement in seen_indices:
            for i in seen_indices[complement]:
                result.append([i, j])

        if value not in seen_indices:
            seen_indices[value] = []
        seen_indices[value].append(j)

    return result


def main() -> None:
    nums = [2, 7, 11, 15, 7, -2, 9]
    target = 9

    print("nums:", nums)
    print("target:", target)
    print()

    print("twoSumLoops:", twoSumLoops(nums, target))
    print("twoSumDict:", twoSumDict(nums, target))
    print("twoSumLoopsAll:", twoSumLoopsAll(nums, target))
    print("twoSumDictAll:", twoSumDictAll(nums, target))


if __name__ == "__main__":
    main()
