def isLeapYear(year):
    if year<1918:
        return year%4==0
    else:
        if year%400==0:
            return True
        if year%100==0:
            return False
        if year%4==0:
            return True
    return False;

def dayOfProgrammer(year):
    if isLeapYear(year):
        return '12.09.' + str(year)
    else:
        if year==1918:
            return '26.09.' + str(year)
        else:
            return '13.09.' + str(year)

if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result + '\n')
