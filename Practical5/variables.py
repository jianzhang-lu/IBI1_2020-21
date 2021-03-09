a=180702
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
if(d>e):
    print("d is greater")
elif(d==e):
    print("they are the same")
else:
    print("e is greater")
#d is greater


X=True
Y=True
Z=(X and not Y)or(Y and not X)
print(Z)
#Z is false because both X and Y are true.
W=(X!=Y)
print(W,type(W))
#W and Z are always the same.

