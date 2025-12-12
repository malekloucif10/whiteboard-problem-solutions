# Author: Mohamed Malek Loucif
# Date: 2025-12-05
# Lab Section: D
# Description: Solves FizzBuzz with an extra Bazz rule using two different approaches.

from typing import List


def fizzBuzzModulus(n: int) -> List[str]:
    result: List[str] = []
    for i in range(1, n + 1):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        if i % 7 == 0:
            out += "Bazz"
        if out == "":
            out = str(i)
        result.append(out)
    return result


def fizzBuzzDict(n: int) -> List[str]:
    mapping = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    result: List[str] = []
    for i in range(1, n + 1):
        out = ""
        for divisor, word in mapping.items():
            if i % divisor == 0:
                out += word
        if out == "":
            out = str(i)
        result.append(out)
    return result


def main() -> None:
    n_str = input("Enter a positive integer for FizzBuzz: ")
    try:
        n = int(n_str)
    except ValueError:
        print("Invalid integer.")
        return
    print("fizzBuzzModulus:", fizzBuzzModulus(n))
    print("fizzBuzzDict:", fizzBuzzDict(n))


if __name__ == "__main__":
    main()
