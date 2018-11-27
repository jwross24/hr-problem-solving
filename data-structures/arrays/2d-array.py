import os


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_sum = -64
    max_hourglass_sum = -64

    for row in range(1, 5):
        for col in range(1, 5):
            hourglass_sum = sum(arr[row-1][col-1:col+2]) + \
                arr[row][col] + sum(arr[row+1][col-1:col+2])
            if hourglass_sum >= max_hourglass_sum:
                max_hourglass_sum = hourglass_sum

    return max_hourglass_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
