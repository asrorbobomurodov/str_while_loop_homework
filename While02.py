def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = len(s)
    i = 0
    n = 0
    while l>0:
        l -= 1
        if s[i].isalpha():
            n += 1
        i += 1
    return n
print(main("python 2022"))