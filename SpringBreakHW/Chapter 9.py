def tuple((a,b), (c,d)):
    if (a+b)*(c+d) >= 25:
        print("greater than or equal to 25")
    else:
        print("less than 25")

print(tuple(3,4), (12,6))