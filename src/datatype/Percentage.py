def percentage():
    N= int(input())
    student= dict()
    for _ in range(N):
        name,*line=input().split()
        scores=list(map(float,line))
        student[name]= scores

    inputStr= input()
    print("%.2f" %(sum(student[inputStr])/3))


percentage()