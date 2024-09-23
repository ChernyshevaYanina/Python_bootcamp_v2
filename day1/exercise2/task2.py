def palindrome(num: int) -> bool:
    if num < 0:
        return False
    reversed_num: int = 0
    temp: int = num
    while temp != 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    return num == reversed_num


def main():
    num: int = int(input())
    print(palindrome(num))


if __name__ == '__main__':
    main()
