
number= input("Enter a number : ") 
if number.isdigit():
    if int(number)%2 == 0 :
        print (f"{number} is EVEN" )
    elif int(number)%2 != 0 :
        print (f"{number} is ODD")
else:
    print("exit")
   
   


    

