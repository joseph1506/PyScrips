from functools import reduce
add10 = lambda x:x+10
print(add10(20))
mult = lambda x,y:x*y
print(mult(10,20))
a= [1,2,3,4,5,6]
b= map(lambda x:x*2,a)
print(list(b))
c= filter(lambda x:x%2==0,a)
print(list(c))
d = reduce(lambda x,y:x*y,a)
print(d)