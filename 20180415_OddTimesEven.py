import re

def is_integer(num):
    if re.fullmatch(r'[0-9]+', num):
        return True
    return False

def is_even(num):
    if num % 2 is 0:
        return True
    return False

def split(num):
    if not is_even(num):
        print("No")
        return False
    length = num // 2
    num = num
    for i in range(1, length + 1):
        if num % (2*i) is 0:
           x = int(num/(2*i))
        else:
            continue

        if not is_even(x):
            print(x, 2*i)
            return

def main():
    while True:
        line_num = input("请输入测试样例数: ").strip()
        if not is_integer(line_num):
            continue

        count = int(line_num)
        nums = []
        while count:
            num = input("请输入测试样例: ").strip()
            if is_integer(num):
                nums.append(int(num))
            else:
                print("输入错误, 重新输入")
                continue
            count -= 1

        for n in nums:
            split(n)

if __name__ == '__main__':
    main()
