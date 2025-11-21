information={
    '1':'31',
    '2':'28',
    '3':'31',
    '4':'30',
    '5':'31',
    '6':'30',
    '7':'31',
    '8':'31',
    '9':'30',
    '10':'31',
    '11':'30',
    '12':'31'}
print (information)

month=input("input the month number:")#asks user to input the number of the month

if month == '1':
   print (information['1'])
elif month == '2':
      input( "is this a leap year")
      if True: #input the answer true if true
        print (29)
      if False:
            print (28)
elif month == '3':
    print (information['3'])#prints the dictionary 3 and its information
elif month == '4':
    print (information['4'])
elif month == '5':
    print (information['5'])
elif month == '6':
    print (information ['6'])
elif month == '7':
    print (information['7'])
elif month == '8':
    print (information ['8'])
elif month == '9':
    print (information ['9'])
elif month == '10':
    print (information['11'])
elif month == '11':
    print (information['11'])
elif month == '12':
    print (information['12'])


