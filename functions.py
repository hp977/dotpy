# Use def to define function 

# def square(x,y,z): 
# for multiple input

def square(x): 
    return x * x
for i in range(10): 
    print(f"The square of {i} is {square(i)}")

# To import function from another file 
# from function import square 
# where function is the name of file you want to import from

# or 
import functions
for i in range(10): 
    print(f"The square of {i} is {square(i)}")

    # prints out the same result
    
