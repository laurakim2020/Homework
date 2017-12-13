import sys

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
        
test_suite()
    

    
            
        
        
        
        


            
            
        



        
