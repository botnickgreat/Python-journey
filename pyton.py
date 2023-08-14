def calculate_taxi_cost(driver_name, has_discount=False, **kwargs):
# Extract the values from kwargs
  client_name = kwargs['client_name']
  trip_time = kwargs['trip_time']
  patrol_cost = kwargs['patrol_cost']

# Calculate the base fare
  base_fare = trip_time * 10

# Apply discount if applicable
  if has_discount:
    base_fare *= 0.9

# Calculate the total cost
  total_cost = base_fare + patrol_cost
  print(f'Total cost for {driver_name} is {total_cost}')

# Example function call
calculate_taxi_cost('John', has_discount=True, client_name='Alice', trip_time=30, patrol_cost=20)
calculate_taxi_cost('Alex', client_name='Max', trip_time=10, patrol_cost=30)

# Define a function with arbitrary arguments
def merge_string_lists(*args):
    merged_string = ''

# Iterate all strings in args
    for string_list in args:
        merged_string += ' '.join(string_list) + ' '

# Return resulting string
    return merged_string

# Example usage
list1 = ['Hello,', 'world!']
list2 = ['I', 'am', 'Python!']
list3 = ['Nice', 'to', 'meet', 'you!']
result = merge_string_lists(list1, list2, list3)
print(result)

def calculate_statistics(numbers):
    if len(numbers) == 0:
        return 0, 0, 0, 0
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum

# Example usage
data = [12, 7, 15, 9, 22, 13, 18]
total, average, minimum, maximum = calculate_statistics(data)

print(f'Total Sum: {total}')
print(f'Average: {average:.4f}')
print(f'Minimum Value: {minimum}')
print(f'Maximum Value: {maximum}')
