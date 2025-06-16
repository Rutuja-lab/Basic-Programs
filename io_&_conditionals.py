# 1. Write a Python program to check whether a 
# number is positive, negative or zero.

print("Example 1. A Python program to check whether" \
" a number is positive, negative or zero.")

# taking input from an user
num = int(input("Enter any number : "))
if ((num)>0):
     print(f"The number {num} is positive")
elif (num<0):
     print(f"The number {num} is negative")
elif (num==0):
     print(f"The number is zero")
# else:
#    print("Please input a number") 

# 2. Take marks of 3 subjects and print the average.
#  Also, print grade based on average.

print("\nExample 2. Take marks of 3 subjects and print the average. Also, print grade" \
" based on average.")

# Taking the marks from the user
maths = int(input("Enter marks that you scored in " \
"mathematics : "))
science = int(input("Enter marks that you scored in " \
"science : "))
accounts = int(input("Enter marks that you scored in " \
"accounts : "))
average = (maths + science + accounts)/3

if(average<0 or maths<0 or science<0 or accounts<0):
    print("Invalid marks have been input")    
elif(100>=average>=90):
    print(f"The average of your marks is {average}")
    print("Your grade based on your marks is " \
    "Ex")
elif(90>=average>=80):
    print(f"The average of your marks is {average}")
    print("Your grade based on your marks is " \
    "A")
elif(80>=average>=70):
    print("Your grade based on your marks is " \
    "B")
elif(70>=average>=60):
    print(f"The average of your marks is {average}")
    print("Your grade based on your marks is " \
    "C")
elif(60>=average>=50):
    print(f"The average of your marks is {average}")
    print("Your grade based on your marks is " \
    "D")
elif(average<50):
    print(f"The average of your marks is {average}")
    print("Your grade based on your marks is " \
    "F")
      


# 3. Write a program to find the greatest among 
# three numbers entered by the user.

print("\nExample 3. A program to find the greatest " \
"among three numbers entered by the user")

# Taking input from user
num_1 = int(input("Enter number 1 : "))
num_2 = int(input("Enter number 2 : "))
num_3 = int(input("Enter number 3 : "))
if(num_1 == num_2 == num_3):
    print("The numbers you entered are all equal")
elif((num_1>=num_2) and (num_1>=num_3)):
    print(f"The greatest number among the three "  
          f"numbers is {num_1}")
elif((num_2>=num_1) and (num_2>=num_3)):
    print(f"The greatest number among the three " 
          f"numbers is {num_2}")
elif((num_3>=num_2) and (num_3>=num_1)):
    print(f"The greatest number among the three "  
          f"numbers is {num_3}")
    