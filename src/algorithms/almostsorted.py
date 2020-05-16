# Complete the almostSorted function below.
def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True


def almostSorted(arr):
    if isSorted(arr):
        print('yes')
        return
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    almostSorted(arr)
