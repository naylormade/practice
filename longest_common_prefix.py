def longestCommonPrefix(strs) -> str:
    ppref = ""
    
    if not strs: return ""  #empty string
    if len(strs) == 1: return strs[0]  #only 1 given string
    if strs: first_word = strs[0]  #initialize first word
    if first_word == "":  #if given an empty string but empty
        return ""
    for word in strs[1:]:
        indexes = 0
        for letter in word:
            if letter == first_word[indexes]:
                ppref += letter
                indexes += 1
            else:
                print("No match on 2nd word so ending")
                return ""
    if ppref:
        print(f'ppref: {ppref}')
        return ppref
    

longestCommonPrefix(["flower","flow","flight"])