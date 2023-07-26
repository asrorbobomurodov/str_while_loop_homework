def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
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
            if int(s[i])%2==0:
                yigindi += 1
        i += 1
    return yigindi
print(main("141531a234"))
