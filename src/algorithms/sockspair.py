def sockMerchant(n, ar):
    pairs=dict()
    for i in ar:
        pairs[i]=pairs[i]+1 if i in pairs else 1
    count=0
    for i in pairs:count+=int(pairs[i]/2)
    return count

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(str(result) + '\n')
