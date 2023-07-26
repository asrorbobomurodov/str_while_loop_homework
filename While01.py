def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = len(s)
    n = 0
    i = 0
    while l>0:
        l = l-1
        if s[n].isdigit():
            i = i+1
        n = n + 1
    return i
print(main("a24bc"))
print(main("python 2022"))