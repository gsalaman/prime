# Next improvement: stop at sqrt.
from math import sqrt, floor

# prime number definition...only divisibly by 1 and itself. 

# count from 2 up to top_candidate
top_candidate = 100

prime_set = []

# next version:  check factors from 2 up to the square root of our candidate.  
for candidate in range(2,top_candidate):

  # Start by assuming the number is prime
  prime = True

  top_factor = floor(sqrt(candidate))

  # check the factors from 2 up to and including the sqrt of our candidate 
  for factor in range (2, top_factor+1):
    if (candidate % factor == 0):
      prime = False
      break;
  
  # Okay, we've now either checked all the factors, or we've hit one that was
  # divisible.  
  if (prime):
    print("Prime found:  ", candidate)
    prime_set.append(candidate)
  else:
    print(candidate, " was not prime")

print("============")
print("Our primes")
print(prime_set)
