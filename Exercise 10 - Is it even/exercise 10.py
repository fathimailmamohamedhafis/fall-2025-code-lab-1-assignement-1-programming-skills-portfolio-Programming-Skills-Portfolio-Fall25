x= int(input("input your number here:")) #asks user to input number
 
def even_or_odd(x): #decides if function is even or odd 
    if x % 2 == 0: #finds the remainder when x is divided by 2
        return "even" #funtion will return even
    else:
        return "odd" #function will return odd
print  (even_or_odd(x)) #prints whether the number is even or odd