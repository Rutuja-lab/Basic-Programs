# 10. Input a string and count the number of vowels
# in it.

print("Example 10. Input a string and count the " \
"number of vowels in it")
string = input("Enter any word or sentence : ")
count = 0
for i in string:
    if (i == "a" or i == "e" or i == "i" or 
        i == "o" or i == "u"):
        count += 1
print(f"The number of vowels in entered string"
       f" is {count}")       

# 11. Write a Python program to check if a string 
# is a palindrome.

print("\nExample 11. a Python program to check if a " \
"string is a palindrome")
my_string = input("Enter any word or number : ")
rev_string = ""
for i in range((len(my_string))-1,-1,-1):
    rev_string += my_string[i]
# print(rev_string)    
if (rev_string == my_string):
    print(f"{my_string} is a palindrome")
else:
    print(f"{my_string} is not a palindrome") 

# 12. Remove all duplicate characters from a string 
# (keep only first occurrences).

print("\nExample 12. Remove all duplicate characters" \
" from a string (keep only first occurrences).")
my_string = input("Enter any sentence or word or " \
"number : ")
result = ""
result_set = set()
for i in my_string:
    if not i in result_set:
        result_set.add(i)
        result += i
    else:
        pass
print(f"The string with duplicate characters removed"
 f" is {result}")        
