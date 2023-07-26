def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = len(s)
    i = 0
    odds = 0
    while l>0:
        l -= 1
        if s[i].isdigit():
            if int(s[i])%2==1:
                odds += 1
        i = i+1
    return odds
print(main("asr5896"))