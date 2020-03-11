"""LAB1
CPE202
"""

# import unittest

#1
def get_max(int_list):
    """find the maximum in a list of integers
    Args:
        int_list (list): a list of integers
    Returns:
        int: max integer
    """
    max_int = 0
    if len(int_list) == 0:
        return None
    for i in range(len(int_list)):
        if int_list[i] > max_int:
            max_int = int_list[i]
    return max_int

#2
def reverse(in_str):
    """reverse a string recursively w/o reverse string library
    Args:
        in_str (str): a string to reverse
    Returns:
        str: the reversed string
    """
    if len(in_str) == 0:
        return in_str
    return reverse(in_str[1:]) + in_str[0]

#3
def search(slist, targ):
    """find index of target integer in sorted list recursively
    Args:
        slist (list): sorted list of integers
        targ (int): value to search for
    Returns:
        int: index of largest integer
    """
    low = 0
    high = len(slist)
    mid = len(slist)//2
    return search_helper(slist, targ, low, mid, high)

def search_helper(slist, targ, low, mid, high):
    """helps search function find index of target integer in sorted list recursively
    Args:
        slist (list): sorted list of integers
        targ (int): value to search for
        low (int): lowest index of array
        mid (int): dynamic mid index used to find target
        high (int): largest index of array
    Returns:
        int: index of largest integer
    """
    if low == mid or mid == high-1 or slist == []:
        if slist and (slist[mid] == targ):
            return mid
        return None
    if slist[mid] == targ:
        return mid
    if slist[mid] > targ:
        mid = mid//2
        return search_helper(slist, targ, low, mid, high)
    # else slist[mid] > targ
    mid = (mid+high)//2
    return search_helper(slist, targ, low, mid, high)

#4
def fib(term):
    """find the value of the nth fibonacci number
    Args:
        term (int): the nth term to calculate fibonacci
    Returns:
        int: value of nth fibonacci number
    """
    if term == (1 or 2):
        return 1
    if term > 1:
        return fib(term-1) + fib(term-2)
    return 0

#5.1 factorial iterative version
def factorial_iter(nth):
    """calculate the nth factorial iteratively
    Args:
        n (int): the nth factorial to be calculated
    Returns:
        int: value of the nth factorial
    """
    res = 0
    if nth < 2:
        return 1
    while nth > 2:
        res += nth*(nth-1)
        nth = nth-1
    return res

#5.2 factorial recursive version
def factorial_rec(nth):
    """calculate the nth factorial recursively
    Args:
        n (int): the nth factorial to be calculated
    Returns:
        int: value of the nth factorial
    """
    if nth <= 1:
        return 1
    return nth*factorial_rec(nth-1)
