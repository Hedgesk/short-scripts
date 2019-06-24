def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    total = 0
    for i in range(0, len(s)):
        letter = s[i]
        if letter == "M":
            total += 1000
        if letter == "D":
            if i < len(s) - 1 and s[i + 1] in ["M"]:
                total -= 500
            else:
                total += 500
        elif letter == "C":
            if i < len(s) - 1 and s[i + 1] in ["M", "D"]:
                total -= 100
            else:
                total += 100
        elif letter == "L":
            if i < len(s) - 1 and s[i + 1] in ["M", "D", "C"]:
                total -= 50
            else:
                total += 50
        elif letter == "X":
            if i < len(s) - 1 and s[i + 1] not in ["I", "V", "X"]:
                total -= 10
            else:
                total += 10
        elif letter == "V":
            if i < len(s) - 1 and s[i + 1] not in ["I", "V"]:
                total -= 5
            else:
                total += 5
        elif letter == "I":
            if i < len(s) - 1 and s[i + 1] not in ["I"]:
                total -= 1
            else:
                total += 1
    return total


if __name__ == '__main__':
    print(romanToInt("III"))
    print(romanToInt("IV"))
    print(romanToInt("IX"))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))