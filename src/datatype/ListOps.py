def operations():
    items = list()
    for _ in range(int(input())):
        operation,*operands= input().split()
        params= list(map(int,operands))
        if operation == 'insert':
            items.insert(params[0],params[1])

        if operation =='print':
            print(items)

        if operation =='remove':
            items.remove(items[0])

        if operation == 'append':
            items.append(items[0])

        if operation=='sort':
            items.sort()

        if operation == 'pop':
            items.pop()

        if operation == 'reverse':
            items.reverse()

