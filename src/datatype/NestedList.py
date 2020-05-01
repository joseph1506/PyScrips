def secondLowest():
    N = int(input())
    nameScore= dict()
    for _ in range(N):
        name= input()
        score = float(input())
        nameScore[name]=score

    secondLowScore = sorted(set(nameScore.values()))[1]
    names= sorted([key for key in nameScore if nameScore[key]==secondLowScore])
    for i in names:
        print(i)


secondLowest()

