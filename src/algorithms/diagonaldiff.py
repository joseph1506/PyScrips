def diagonalDifference(arr):
    sumR=0
    sumL=0
    for i in range(len(arr)):
        sumR+=arr[i][i]
        sumL+=arr[i][len(arr)-(i+1)]

    return abs(sumR-sumL)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)