def gradingStudents(grades):
    result=[]
    for i in grades:
        if i<38 or i%5==0 or i%5<=2:
            result.append(i)
        else:
            div= int(i/5)
            result.append((div+1)*5)
    return result

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print('\n'.join(map(str,result)))

