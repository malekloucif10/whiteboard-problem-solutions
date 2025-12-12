# Author: Mohamed Malek Loucif
# Date: 2025-12-05
# Lab Section: D
# Description: Reverses a string iteratively and recursively.


def reverseIterative(s: str) -> str:
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return "".join(chars)


def reverseRecursive(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[-1] + reverseRecursive(s[:-1])


def main() -> None:
    text = input("Enter a string to reverse: ")
    print("reverseIterative:", reverseIterative(text))
    print("reverseRecursive:", reverseRecursive(text))


if __name__ == "__main__":
    main()
