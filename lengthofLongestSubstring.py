def lengthOfLongestSubstring(s: str) -> int:
    curr_start = 0
    curr_end = 0
    max_start = 0
    max_end = 0
    letters = set()
    max_count = 0
    for idx in range(len(s)):
        if s[idx] in letters:
            pos = s[curr_start:curr_end].find(s[idx])
            letters = letters - set(s[curr_start:curr_start + pos])
            curr_start = curr_start + pos+1
            curr_end = idx +1
        else:
            letters.add(s[idx])
            curr_end = idx + 1
            if max_count < len(letters):
                max_count = len(letters)
                max_start = curr_start
                max_end = curr_end

    #print("------------------------------")
    #print(max_start, max_end)
    #print(max_count)
    #print(s[max_start:max_end])
    return max_count


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))

    print(lengthOfLongestSubstring("bbbbbbb"))
