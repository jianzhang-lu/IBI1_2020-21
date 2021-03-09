# int the origin value a=1, b=1
# repeat for another 11 times
# int again: if it is the odd time: a=a+b
#            if it is the even time: b=a+b
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

