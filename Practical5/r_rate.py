# Int n =84
# We should input the value of r manually
# Repeat 5 times and every time let new n=n*r+n
# Since the type of content in the input is str, we should convert it to double or int to do calculate.
# Print the sentence we need. 


n=84
r=float(input("the rate of reproduction of a virus:"))
for i in range(0,5):
    n=n*r+n
print("The rate of reproduction of a virus is",r,", and the total number of individuals infected after 5 generations is "
