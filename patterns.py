# 7. Print the following pattern:
# *
# * *
# * * *
# * * * *
print("Example 7.")
n = int(input("Enter any number : "))
for i in range(1,n+1):
        print("*"*i)

# 8. Print this pattern for n=5:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("\nExample 8.")
n = 5
for i in range(1,n+1):
        for j in range(1,i+1):
                print(j,end="")
        print()        
       
# 9. Print inverted triangle pattern using stars 
# (for n rows).
print("\nExample 9.")
n = 5
for i in range(n,0,-1):
        for j in range(1,i+1):
                print(j,end="")
        print()