def bonAppetit(bill, k, b):
    annabill = int((sum(bill)-bill[k])/2)
    return 'Bon Appetit' if annabill==b else (b-annabill)

if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)