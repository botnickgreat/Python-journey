var1 = 100
# Try to redefine the value to 150
var1 = 150

# Print the var1 variable
print(var1)
var1 = 91400000
var2 = 238855

# Print the corrected variables
print("The initial var1 was 91,400,000 and the corrected is:", var1)
print("The initial var2 was 238 855 and the corrected is:", var2)
number1 = 167 - 98j
number2 = 67 + 9j
number3 = 186282

# Print the real part of the number1 variable
print("The real part of the number1 =", number1.real)
# Print the imaginary part of the number2 variable
print("The imaginary part of the number2 =", number2.imag)
# Print the number 3 variable in a complex form
print("The speed of light =", number3.real + number3.imag *1j)

# Calculate the number of task that will be completed
completed = 60 // 7
# Calculate the number of minutes that will left
minutes = 60 % 7

# Print the result
print("The number of completed tasks is", completed)
print("The number of remaining minutes is", minutes)

completed = 60 // 7
minutes = 60 % 7
# Calculate the number of remaining tasks
remaining_tasks = 10 - completed
# Calculate how many minutes you need to complete all tasks
required_time = 10 * 7 

# Print the result
print("The number of remaining tasks is",  remaining_tasks)
print("The number of minutes for completing the tasks is", required_time)

number1 = 88/16e-1
number2 = 12/2

# Print the number and it's type
print("The value of number1 is", number1)
print("The type of number1 is", type(number1))
print("The value of number2 is", number2)
print("The type of number2 is", type(number2))
number1 = 56432e-4
number2 = (45 - 2j)
number3 = 365

# Output the type of the sum of float number and integer number
print(type(number1 + number3))
# Output the type of the multiplication of complex number and integer number
print(type(number2 * number3))
# Output the type of the float number subtracted from the integer number
print(type(number3 - number1))
