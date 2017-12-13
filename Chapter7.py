list=[3,5,-4,3,17,9]
wordlist=["sushi","pizza","popcorn","noodles"]
samlist= ["sam","chloe","annie","sam"]

#Write a function to count how many odd numbers are in a list.
def count_odd(list):
    count = 0
    for i in list:
        if i%2 != 0:
            count += 1           
    return count
print(count_odd(list))

#Sum up all the even numbers in a list.
def sum_even(list):
    mysum=0
    for i in list:
        if i%2 == 0:
            mysum = mysum +i           
    return mysum
print(sum_even(list))

#Sum up all the negative numbers in a list.
def sum_neg(list):
    mysum=0
    for i in list:
        if i<0:  
            mysum = mysum + i                     
    return mysum
print(sum_neg(list))

#Count how many words in a list have length 5.
def len_five(list):
    words = 0
    for i in list:
        if len(i)== 5:
            words += 1
    return words
print(len_five(wordlist))    
    
#Sum all the elements in a list up to but not including the first even number.
def sum_first(list):
    mysum = 0
    for i in list:
        if i%2 == 0:
            break
        else:
            mysum +=i
    return mysum
print(sum_first(list))

#Count how many words occur in a list up to and including the first occurrence of the word “sam”
def word_sam(samlist):
    count = 0
    for i in samlist:
        if i == "sam":
           count += 1
           break
        count += 1
    return count
print(word_sam(samlist))
        
            
                      
    

    
            
        
        
        
        


            
            
        



        
