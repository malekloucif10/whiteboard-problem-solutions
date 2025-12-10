# Author: Mohamed Malek Loucif
# Date: 2025-12-05
# Lab Section: D
# Description: Checks if a list of integers contains any duplicates.

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def main() -> None:
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([]))
    print(contains_duplicate([5, 5, 5]))


if __name__ == "__main__":
    main()
