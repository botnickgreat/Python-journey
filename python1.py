def geometric_progression(a, r):
    while True:
        yield a
        a *= r
        
geo_gen = geometric_progression(2, 3)

# Generate and print the first 5 terms of the geometric progression
for i in range(5):
    print(next(geo_gen))
