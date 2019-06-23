# Author: Abhishek Sharma
# Question: Given an input as array of integers, and you have to reorder its entries so that even entries appear first.
# Reference: Element of Programming Interview Python


# Simple Approach: Time Complexity is O(N), Space Complexity O(2N)
def simple_even_odd(A):
    ls = []
    for i in A:
        if i % 2 == 0:
            ls.insert(0, i)
        else:
            ls.append(i)
    return ls


# Optimized Approach: Time Complexity is O(N), Space Complexity O(1)
def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A


print("Simple Approach", simple_even_odd([1, 2, 3, 4, 5, 6]))
print("Optimized Approach", even_odd([1, 2, 3, 4, 5, 6]))