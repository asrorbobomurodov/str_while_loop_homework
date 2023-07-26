def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = len(s)
    i = 0
    summa = 0
    while l>0:
        l = l-1
        if s[i].isdigit():
            if int(s[i])%2==1:
                summa = summa + int(s[i])
        i = i+1
    return summa
print(main("AS1741"))