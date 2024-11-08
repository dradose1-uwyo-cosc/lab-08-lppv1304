# Luna Perez
# UWYO COSC 1010
# 11/07/2024
# Lab 08
# Lab Section:13
# Sources, people worked with, help given to: https://www.geeksforgeeks.org/type-isinstance-python/, https://stackoverflow.com/questions/40387485/quadratic-formula-without-import-math, 
#https://www.calculator.net/quadratic-formula-calculator.html, 
# Didnt know how to solve quadratic equation so had to learn that
# 
# 


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
prompt = "Give me a string of number or floats and ill convert them: "
test_string= input(prompt)

def int_check(value):
    """"check strings and if they are ints or floats convert them"""
    isneg= False
    if "-" in value:
        isneg= True
        value = value.replace('-','')
    try:
        if isneg:
            return -1*int(value)
        else:
            int_val = int(value)
            return int_val
    except:
        ValueError
        print("Error: Only numbers please")
    try:
        if "." in value: 
            value_list = value.split('.')
            if len(value_list) == 2 and value_list[0].isdigit() and value_list[1].isdigit:
                 if isneg:
                    return -1* float(value)
                 else:
                    return float(value)
    except:
        ValueError

result = int_check(test_string)
print(result)
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
slope_prompt= "Give me 4 values\nIll take those values and put them into the slope intercept formula\nPlease format it 'm b upper x lower x: "
def slope_intercept(m,b,up_x,lo_x):
    '''Does the algebraic equation Point slope and returns a list of y values for a given range of x'''
    y_values=[]
    for x in range(lo_x,up_x + 1):# the plus one was the only way i could think to make it inclusive 
        y = m * x+ b
        y_values.append(y)
    return y_values
while True:
    user_input= input(slope_prompt)
    if user_input == 'exit'.lower():
        break
    try:
        m,b,up_x,lo_x = user_input.split()
        m = int_check(m)
        b = int_check(b)
        up_x = int_check(up_x)
        lo_x= int_check(lo_x)
        if m is False or b is False or up_x is False or lo_x is False: 
            print("only Numbers allowed")
            continue
        if isinstance(up_x,float) or isinstance(lo_x,float):
            print("x ranges cannont be floats")
            continue
        y_range = slope_intercept(m, b ,up_x, lo_x)
        print(f"The y range of the given {lo_x},{up_x}, is = {y_range}")
    except ValueError:
        print("Please use the m b up_x lo_x format")
        continue
    

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
#
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def square_rt(x):
    '''Give the Square root for the given number'''
    return x ** 0.5
def quad_form(a,b,c):
    d = b**2 - 4*a*c
    if d <0:
        return "no real roots"
    elif d == 0:
        x = -b / (2*a)
        return x 
    else:
        x1 = (-b + square_rt(d)) / (2*a)
        x2 = (-b - square_rt(d)) / (2*a)
        return x1, x2 

q_prompt = "give me three inputs and ill use them in the quadratic formula\n Please format using a b c : "

while True:
    user_input_q= input(q_prompt)
    if user_input_q.lower == exit:
        break
    a,b,c = user_input_q.split()
    a = int_check(a)
    b = int_check(b)
    c = int_check(c)
    print(quad_form(a,b,c))