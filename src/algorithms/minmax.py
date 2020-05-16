# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sumA= sum(arr)
    min,max=sumA-arr[0],sumA-arr[0]
    for i in range(0, len(arr)):
        print(i)
        if sumA-arr[i]>max:
            max= sumA-arr[i]
        if sumA-arr[i]<min:
            min= sumA-arr[i]
    print("{} {}".format(min,max))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
