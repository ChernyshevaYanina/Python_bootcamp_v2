def pascal_triangle() -> None:
    try:
        nums:int = int(input())
        num:list = [1]
        for i in range(nums):
            print(" ".join(str(x) for x in num))
            num = [sum(x) for x in zip([0]+num, num+[0])]
    except:
        print("Natural number was expected")


def main():
    pascal_triangle()


if __name__ == '__main__':
    main()
