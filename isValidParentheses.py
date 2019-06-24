def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if (len(s) == 0):
        return True

    stack = ""

    for i in range(0, len(s)):
        if s[i] == "(":
            stack += "("
        elif s[i] == "{":
            stack += "{"
        elif s[i] == "[":
            stack += "["
        elif s[i] == ")":
            if len(stack) == 0 or stack[len(stack) - 1] != "(":
                return False
            else:
                stack = stack[:-1]
        elif s[i] == "}":
            if len(stack) == 0 or stack[len(stack) - 1] != "{":
                return False
            else:
                stack = stack[:-1]
        elif s[i] == "]":
            if len(stack) == 0 or stack[len(stack) - 1] != "[":
                return False
            else:
                stack = stack[:-1]
        else:
            return False

    if len(stack) > 0:
        return False
    return True


if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("([)]"))
    print(isValid("{[]}"))