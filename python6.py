# Data
people = [["Alex", 178], ["Noah", 189], ["Peter", 175], ["John", 185], ["Michelle", 165]]

# Iterating over external list
for i in range(len(people)):
    if type(people[i]) is list:
        # Calculate and round height in inches
        ht_in = round(people[i][1]/2.54, 2)
        print(people[i][0], 'has height of', ht_in, 'inches')
        
        def my_first_function(a, b, c):
  return((3*a + 2*b + c)**2) 

# Testing the function
print(my_first_function(5,4,3))
# Define a function
def is_positive(n):
  if n > 0 :
    return('positive')
  elif n < 0:
    return('negative')
  else:
    return('zero')

# Test your function on -5, 0 and 5
print('Number -5 is', is_positive(-5))
print('Number 0 is', is_positive(0))
print('Number 5 is', is_positive(5))
