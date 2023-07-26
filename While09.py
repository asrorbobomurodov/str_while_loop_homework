def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = len(s)
    i = 0
    yigindi = 0
    while l>0:
        l -= 1
        if s[i].isdigit():
            yigindi += int(s[i])
        i += 1
    return yigindi
print(main("145874"))