import math

def isPalindrome(x: int) -> bool:
    #have to compare numbers up until the 1/2 way point
    input_as_str = str(x)
    str_length = len(input_as_str)
    for idx,num in enumerate(input_as_str[:math.ceil(str_length / 2)]):
        if num != input_as_str[-(idx+1)]:         
            print("False")
            return False
    print("True")    
    return True