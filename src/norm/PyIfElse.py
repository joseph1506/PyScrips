N = int(input())
if N%2 is not 0:
    print("Weird")

if N%2 is 0:
    if N<=5 and N>=2:
        print("Not Weird")

    if N<=20 and N>=6:
        print("Weird")

    if N>20:
        print("Not Weird")
