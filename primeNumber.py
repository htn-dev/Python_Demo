print('Prime numbers between 1 and 250 are:')

for possiblePrime in range(2, 250):    
    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False    
            
    if isPrime:
        print(possiblePrime)
