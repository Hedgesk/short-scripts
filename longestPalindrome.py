def longestPalindrome(s: str) -> str:
    #print(s)
    curr_start = 0
    max_start = 0
    max_end = 1
    max_len = 1
    for idx in range(len(s)):
        curr_range = min(idx +1 - curr_start, max_len)
        for jdx in range(curr_start, idx +1- curr_range):
            test = True
            for t in range(int((idx+1-jdx) / 2)):
                if s[jdx + t] != s[idx+1 - t - 1]:
                    test = False
            #print(s[jdx:idx+1],test)
            if test and max_len < idx+1 - jdx:
                max_len = idx+1 - jdx
                max_end = idx+1
                max_start = jdx

    return s[max_start:max_end]

if __name__ == '__main__':
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("bb"))
    print(longestPalindrome("bbb"))
    print(longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
