
print("__ __ __ __ __ __ __ __ __ ___ __ ___ ___ __ __ __ __")
#create a list of math operations so the user can tell the computer what operation they want
print("|1.add,\n|2.subtract,\n|3.multiply,\n|4.divide,\n|5.exit")
#create a loop to keep the calculator running
while True:
    user_input = input("\n|pick a number:")#take input from user so the computer knows which operations we using
    if user_input == "5":
        break#exit the calcultor when the user pick 5
#take a number value from the user
    num1 = float(input("|number: "))#
    num2 = float(input("|number: "))
    
#use if statements to do the math and give the user the answer
    if user_input == "1":
        print("|answer: ", num1 + num2)
        print("\n|Addition")
        print(num1, "+",num2)
    
    elif user_input == "2":
        print("|answer: ", num1 - num2)
        print("\n|Subtraction")
        print(num1,"-",num2)
    
    elif user_input == "3":
       print("|answer: ", num1 * num2)
       print("\n|Multiplication")
       print(num1,"*",num2)
    
    elif user_input == "4":
        if num2 == 0:
           print("can't divide by 0")
        else:
            print("answer: ",num1 / num2)
            print("\n|Division ")
            print(num1,"/",num2)
    else:
       print("|Type in a number")#This is for when the user type in anything that is not listed
    
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")