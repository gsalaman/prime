# Initial algo...just counting up

# prime number definition...only divisibly by 1 and itself. 

# count from 2 up to top_candidate
top_candidate = 100

prime_set = []

for candidate in range(2,top_candidate):
  # brute force version:  check factors from 2 up to our candidate.  
  
  # Start by assuming the number is prime
  prime = True
 
  # check the factors from 2 up to (but not including) our candidate number
  for factor in range (2, candidate):
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
