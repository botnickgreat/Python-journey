# People dictionary
people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

# Define the function
def people_information(d, name):
  print("Name:", name)
  print("Age:", d[name][0], "y.o.")
  print("Height:", d[name][1], "cm")

# Testing the function
people_information(people_d, "Alex")
people_information(people_d, "Michelle")
# People dictionary
people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

# Update the function
def people_information_mod(d, name):
  if name not in d.keys():
    # Check if name doesn't exist in the dictionary keys
    print("There is no information about", name)
  else:
    print("Name:", name)
    print("Age:", d[name][0], "y.o.")
    print("Height:", d[name][1], "cm")

# Test your function
people_information_mod(people_d, "Alex")
people_information_mod(people_d, "Richard")


# Define a lambda function
fun = lambda a, b, c: (3*a + b*2 + c)**2

# Testing the function
print(fun(1, 2, 3))
print(fun(3, 2, 1))
