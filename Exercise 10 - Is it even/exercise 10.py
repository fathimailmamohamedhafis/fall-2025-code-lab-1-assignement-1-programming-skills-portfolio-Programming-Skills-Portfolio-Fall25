x= int(input("input your number here:"))
 
def even_or_odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
print  (even_or_odd(x))