# 1. (a) Develop a module called module_ListFunction that includes the following functions:
# i. A function to find the maximum value in a given list.
# ii. A function to find the minimum value in a given list.
# iii. A function to calculate the sum of all elements in a list.
# iv. A function to compute the average of the list.
# v. A function to determine the median of a list.
# Additionally, create lists using Python comprehension for various scenarios and demonstrate
# the use of the module functions with these lists.
# module_ListFunction.py

def maximum(lst):
    return max(lst)


def minimum(lst):
    return min(lst)


def total_sum(lst):
    return sum(lst)


def average(lst):
    return sum(lst) / len(lst)


def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2

    if n % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) // 2
    else:
        median = sorted_lst[mid]

    return median
