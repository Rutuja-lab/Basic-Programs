# 16. Write a function to find the factorial of a number.

print("Example 16. Write a function to find the factorial" \
" of a number")

#factorial(n) = n * factorial(n-1)
n = int(input("Enter any number : "))
def factorial(n):
    if(n==0):          #base condition - doesn't call fn anymore
        return 1
    else:
        return n * factorial(n-1)
f = factorial(n)    
print(f"Factorial of {n} is {f}") 

# 17. Create a function that checks whether a given
# number is an Armstrong number.

print("\nExample 17. A Python program to check " \
"whether a given number is an Armstrong number")

def is_armstrong(num):
    total = 0
    order = len(str(num))
    original = num
    while num>0:
        digit = num % 10
        total += digit ** order
        num //= 10  # Floor division (removes the decimal and digits after it)
    return total == original
n = int(input("Enter a number: "))
if is_armstrong(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")    

    
# 18. Write a function that takes a list and returns the sum of
# only even numbers.

print("\nExample 18. Write a function that takes a list and returns the sum of " \
"only even numbers")
list = []
l1 = int(input("Enter number 1 : "))
list.append(l1)
l2 = int(input("Enter number 2 : "))
list.append(l2)
l3 = int(input("Enter number 3 : "))
list.append(l3)
l4 = int(input("Enter number 4 : "))
list.append(l4)
l5 = int(input("Enter number 5 : "))
list.append(l5)

def even_sum():
    total = 0
    for i in list:
        if (i % 2 == 0):
            total += i           
    return total    
print(f"The sum of even nos in the list is {even_sum()}")            