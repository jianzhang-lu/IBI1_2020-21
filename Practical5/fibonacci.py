# int the origin value a=1, b=1, 2, 3, 5, 8...
# must repeat for another 11 times
# int again: if it is the odd time: a=a+b, for the first part, a=2,b=1 and print a. 
#            if it is the even time: b=a+b for the second part, a=2,b=3 and print b
# print every value of the first 13 value



a,b=1,1
print(a)
print(b)
for i in range(1,12):
    if(i%2==1):
        a=a+b
        print(a)
    else:
        b=a+b
        print(b)

