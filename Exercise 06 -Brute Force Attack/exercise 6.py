actual_password = "12345" # correct password
chances = 5 # total chances the user has to enter the password

while chances > 0:
    password = input("Enter the password: ").strip() #asks user to input password

    if password == actual_password:   # compare with the variable
        print("Correct password!")
        break #breaks loop
    
    else:
        chances -= 1 #chances will be deducted by one
        if chances > 0:
            print(f"Incorrect Password. ({chances} chances remaining)") #shows how many chances remaining
        else:
            print("Too many failed attempts.") #if too many attempts were made, this will show
     
           

       
          