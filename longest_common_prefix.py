def longestCommonPrefix(strs) -> str:
    #ppref = ""
    
    if not strs: return ""  #empty string
    if len(strs) == 1: return strs[0]  #only 1 given string
    if strs: ppref = strs[0]  #initialize first word
    if ppref == "":  #if given an empty string but empty
        return ""

    ans = ""
    for word in strs[1:]:
        indexes = 0
        for letter in word:
            if letter == ppref[indexes]:
                ans += letter
                indexes += 1
            else:
                if ans:
                    ans = ppref[:indexes]
                    print(f'ans:{ans}')
                    return ans
                print("No match on 2nd word so ending")
                return ""
    if ans:
        print(f'ans: {ans}')
        return ans
    else:
        return ""
    

longestCommonPrefix(["a","a","a"])