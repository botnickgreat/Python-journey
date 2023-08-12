def calculate_average(*args):
  len_args = len(args)
  if len_args == 0:
     return 0
  total = sum(args)
  average = total / len_args
  return average

# Example usage
print(calculate_average(10, 20, 30, 40, 50))
print(calculate_average(5))
print(calculate_average())

def calculate_gravity_force(**kwargs):
    # Check if required parameters are provided
    if 'mass_1' not in kwargs or 'mass_2' not in kwargs or 'distance' not in kwargs:
        print('Required parameters not provided.')
        return None
 
    # Get the values of mass1, mass2, and distance from kwargs
    mass1 = kwargs['mass_1']
    mass2 = kwargs['mass_2']
    distance = kwargs['distance']
    if distance <= 0:
		    return 0
    
    # Calculate the gravitational force
    gravitational_constant = 6.67430e-11
    force = (gravitational_constant * mass1 * mass2) / (distance ** 2)
    
    return force
  
force = calculate_gravity_force(mass_1 =200, mass_2 =500, distance=0.2)
print(f'The resulting force is {force:.4f}')
