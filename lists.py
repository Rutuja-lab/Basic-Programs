# 13. Input 5 numbers in a list and find the maximum and
# minimum value.

print("Example 13. Finding the max and min value"
" in a list")
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
if (l1==l2==l3==l4==l5):
    print("All numbers are equal")
else:
    maximum = max(list)
    print(f"Maximum number is {maximum}")
    minimum = min(list)
    print(f"Minimum number is {minimum}")

# 14. Remove all duplicates from a list entered by 
# the user.

print("\nExample 14. Remove all duplicates from a " \
"list entered by the user")
list = []
l1 = input("Enter element 1 : ")
list.append(l1)
l2 = input("Enter element 2 : ")
list.append(l2)
l3 = input("Enter element 3 : ")
list.append(l3)
l4 = input("Enter element 4 : ")
list.append(l4)
l5 = input("Enter element 5 : ")
list.append(l5)
new_list = []
lset = set()
for i in list:
    if not i in lset:
        lset.add(i)
        new_list.append(i)        
    else:
        pass
print(f"The list with duplicate elements"
       f" removed is {new_list}")    
        
# 15. Reverse a list without using reverse() or slicing.

print("\nExample 15. Reverse a list without using reverse() "
"or slicing")
my_list = ["Political","Sofisticated","Rutuja","Computer"]
rev_list = []
for i in my_list:
    rev_list.insert(0,i)
print(rev_list)    