try:
    a=5/1
    b= 10+'2'
except ZeroDivisionError as e:
    print("Error occured::", e)
except TypeError as e:
    print(e)
else:
    print('finally')