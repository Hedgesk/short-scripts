def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    pos = 1
    if x < 0:
        pos = -1

    x *= pos
    new_x = 0
    tmp = x

    for i in range(0, len(str(x))):
        m = int((tmp % (10 ** (i + 1))) / 10 ** i)
        new_x += m * (10 ** (len(str(x)) - i - 1))
        tmp -= m

    if new_x < 2 ** 31:
        new_x = new_x * pos
        return new_x
    else:
        return 0


if __name__ == '__main__':
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))
