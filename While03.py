def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = len(s)
    i = 0
    yig = 0
    while l>0:
        l = l-1
        if s[i].isalpha() or s[i].isdigit():
            yig = yig+1 
        i = i+1
    r = len(s)-yig
    return r
print(main("123"))
print(main("#hashtag@&"))
