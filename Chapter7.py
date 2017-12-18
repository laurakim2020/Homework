import sys
import turtle

def test(did_pass):
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
  """ Run the suite of tests for code in this module (this file)"""
  
  print("sum except first even")
  test(sum_first(list)== 8)
  
  print("first sam")
  test(word_sam(samlist)== 1)
  
  print("is_prime")
  test(is_prime(11))
  test(not is_prime(35))
  test(is_prime(19911121))

    
list=[3,5,-4,3,17,9]
wordlist=["sushi","pizza","popcorn","noodles"]
samlist= ["sam","chloe","annie","sam"]   

def count_odd(list):
    """Write a function to count how many odd numbers are in a list"""    
    count = 0
    for i in list:
        if i%2 != 0:
            count += 1           
    return count
print(count_odd(list))

def sum_even(list):
    """Sum up all the even numbers in a list"""
    mysum=0
    for i in list:
        if i%2 == 0:
            mysum = mysum +i           
    return mysum
print(sum_even(list))

def sum_neg(list):
    """Sum up all the negative numbers in a list"""
    mysum=0
    for i in list:
        if i<0:  
            mysum = mysum + i                     
    return mysum
print(sum_neg(list))

def len_five(list):
    """Count how many words in a list have length 5"""
    words = 0
    for i in list:
        if len(i)== 5:
            words += 1
    return words
print(len_five(wordlist))    
    
def sum_first(list):
    """Sum all the elements in a list up to but not including the first even number"""
    mysum = 0
    for i in list:
        if i%2 == 0:
            break
        else:
            mysum +=i
    return mysum
print(sum_first(list))

def word_sam(samlist):
    """Count how many words occur in a list up to and including the first occurrence of the word “sam”"""
    count = 0
    for i in samlist:
        if i == "sam":
           count += 1
           break
        count += 1
    return count
print(word_sam(samlist))

def sqrt(n):
    """Ex 7:Newtons square root function -"""
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print("better",better)
        if abs(approx - better) < 0.001:
            return better
        approx = better
print("sqrt",sqrt(25.0))
        
def is_prime(n):
    """Write a function, is_prime, which takes a single integer
    argument and returns True when the argument is a prime number and False otherwise"""
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

wn = turtle.Screen()
"""Ex 12:Drunk pirate problem"""
laura = turtle.Turtle()
steps = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (angle,move) in steps:
    laura.right(angle)
    laura.forward(move)
             
wn = turtle.Screen()
"""Ex 12:turtle draws a house"""
laura.pensize(10)
house = [(270,50), (30, 50), (120,50), (120,50), (225,70.1), (225,50), (225,70.1), (225,50) ]

for (angle,move) in house:
    laura.right(angle)
    laura.forward(move) 

            
test_suite()               