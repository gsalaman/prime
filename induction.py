# Next stop:  do induction 
from math import sqrt, floor

# prime number definition...only divisibly by 1 and itself. 
# We really only need to check the prime factors up to the square root of the
# number itself!

top_candidate = 100

prime_set = []

for candidate in range(2,top_candidate):

  # Start by assuming the number is prime
  prime = True

  top_factor = floor(sqrt(candidate))

  # check the prime factors from 2 up to and including the sqrt of our candidate 
  for factor in prime_set:
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
