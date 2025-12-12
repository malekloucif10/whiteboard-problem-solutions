# Author: Mohamed Malek Loucif
# Date: 2025-12-05
# Lab Section: D
# Description: Checks if a string is a palindrome iteratively and recursively.


def isPalindromeIterative(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def isPalindromeRecursive(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindromeRecursive(s[1:-1])


def main() -> None:
    text = input("Enter a string to check for palindrome: ")
    print("Iterative:", isPalindromeIterative(text))
    print("Recursive:", isPalindromeRecursive(text))


if __name__ == "__main__":
    main()
