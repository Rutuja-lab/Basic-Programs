# 4. Write a Python program to print the sum of all
# even numbers between 1 and 100.
print("Example 4. a Python program to print the sum " \
"of all even numbers between 1 and 100")

sum = 0
for i in range(1,101):
    if (i%2 == 0):
        # To only add even numbers
        sum += i
print(f"The sum of all even numbers between 1 & 100" \
      f" is {sum}")    

# 5. Input a number and check if it is a prime 
# number.

print("\nExample 5. A Python program to check"
" if a number is a prime number")

num = int(input("Enter a number: "))
if num < 2:
    print(f"{num} is not a prime number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break  # Stops the loop immediately
        else:
            print(f"{num} is a prime number")


# 6. Print the factorial of a number using a for 
# loop.

print("\nExample 6. A Python program to calculate" \
" the factorial of a number using a for loop.")

num = int(input("Enter any number : "))
factorial = 1
for i in range(1,num+1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")