def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    pre = ""
    i = 0

    if len(strs) == 0:
        return pre

    while True:
        if len(strs[0]) > i:
            pre += strs[0][i]
        else:
            return pre
        for s in range(1, len(strs)):
            if len(strs[s]) > i:
                if pre[i] != strs[s][i]:
                    return pre[:-1]
            else:
                return pre[:-1]
        i += 1


if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))