# Complete the plusMinus function below.
def plusMinus(arr):
    posP,posN,posZ=0,0,0
    for i in range(len(arr)):
        if arr[i]<0:
            posN+=1
        elif arr[i]>0:
            posP+=1
        else:
            posZ+=1

    print("%.6f" %(posP*1.0/len(arr)))
    print("%.6f" % (posN * 1.0 / len(arr)))
    print("%.6f" % (posZ * 1.0 / len(arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
