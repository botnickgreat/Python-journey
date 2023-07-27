string = "Work your way up!"

# Print the index of the letter p
print(string.find('p'))
# Print the index of the letter y
print(string.find('y'))
# Print the index of the letter r
print(string.find('p'))
string = "It is cool to have a burning desire for studying"

# Find the index of the given words
burning = string.index('burning')
desire = string.index('desire') 
studying = string.index('studying')

# Print the index
print("The index of the word burning is", burning)
print("The index of the word desire is", desire)
print("The index of the word studying is", studying)
string = "It can be painful to learn from mistakes"

# Extract necessary words
painful = string[string.index('painful'):string.index('painful') +7]
mistakes = string[string.index('mistakes'):string.index('mistakes') + 8]
learn = string[string.index('learn'):string.index('learn') + 5]

# Print the word painful
print(painful)
# Print the word mistakes
print(mistakes)
# Print the word learn
print(learn)
