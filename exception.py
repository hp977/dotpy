x = int(input("x:"))
y = int(input("y:"))

result = x/y
print(f"{x}/{y} = {result}")

# If tried to divide by zero, zero division error happen and we can handle the error gracefully by 
# try result = x/y
# except ZerodivisionError: 
# print ("Error: Cannot divide by 0.")

## this is incomplete, need to complete this later. 