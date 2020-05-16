def migratoryBirds(arr):
    count=dict()
    for i in arr:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    print(count)
    minKey=100000000
    maxCount=0
    for key in count.keys():
        if count[key]>maxCount:
            maxCount=count[key]
            minKey=key
        elif count[key]==maxCount and key<minKey:
            minKey=key

    return minKey

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(str(result) + '\n')
