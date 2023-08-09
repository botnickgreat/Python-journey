def print_name():
  print('My name is nick')
  
print_name()

def calculate_triangle_perimeter(a, b, c):
    perimeter = a + b + c
    print(f'The perimeter is {perimeter}')

calculate_triangle_perimeter(2, 3, 5)

def calculate_velocity(distance, time):

    velocity = distance / time
    return velocity

def calculate_kinetic_energy(mass, velocity):

    kinetic_energy = 0.5 * mass * velocity**2
    return kinetic_energy


distance = 100  # meters
time = 10  # seconds
velocity = calculate_velocity(distance, time)

mass = 5  # kilograms
kinetic_energy = calculate_kinetic_energy(mass, velocity)

print(f'Velocity: {velocity} m/s')
print(f'Kinetic Energy: {kinetic_energy} Joules')
