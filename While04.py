def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = len(s)
    i = 0
    yig = 0
    while l>0:
        l -= 1
        if s[i].isupper():
            yig += 1
        i += 1
    return yig
print(main("CodeschoolUz"))