def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    for i in range(0, int(len(str(x)) / 2 + 1)):
        if int(x / pow(10, i)) % 10 != int(x / pow(10, len(str(x)) - i - 1)) % 10:
            return False

    return True


if __name__ == '__main__':
    print(isPalindrome(-121))
    print(isPalindrome(121))
