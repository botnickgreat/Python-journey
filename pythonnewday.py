def calculate_interest(principal, rate, years):
    # Check the types of inputs: check if the type of input belongs to values in tuple
    if type(principal) not in (int, float):
        print('Principal amount must be a number.')
        return 0
    
    if type(rate) not in (int, float):
        print('Interest rate must be a number.')
        return 0
    
    if type(years) is not int:
        print('Number of years must be an integer.')
        return 0
    
    # Calculate the compound interest using built-in functions
    amount = principal * (1 + rate/100) ** years
    interest = amount - principal
    
    # Round the interest to two decimal places using the built-in round() function
    interest = round(interest, 2)
    
    # Return the calculated interest
    return interest


  
print(calculate_interest(2000, '5', 3))
print(calculate_interest(2000, 5, 3))

def calculate_total_cost(price, quantity, discount= 0, tax_rate= 0.1):

    discounted_price = price - (price * discount)
    subtotal = discounted_price * quantity
    total_cost = subtotal + (subtotal * tax_rate)
    return total_cost
  
# Calculate the total cost without discount and with a tax rate of 0.15
cost1 = calculate_total_cost(10, 5, tax_rate=0.15)
print(f'The first cost is {cost1}')

# Calculate the total cost with a 20% discount and the default tax rate
cost2 = calculate_total_cost(10, 5, discount=0.2)
print(f'The second cost is {cost2}') 
