# Given an array, A, of N integers, print each element in reverse order as a
# single line of space-separated integers.

import os


# Complete the reverseArray function below.
def reverseArray(a):
    a.reverse()
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
