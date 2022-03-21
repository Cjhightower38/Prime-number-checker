#Write your code below this line 👇
# Define def
def prime_checker(number):
  # Set flag to true so it runs until it is no longer true
  is_prime = True
  # Iterate through the number from 2 - it's self.
  for item in range(2, number):
    # Use modulus to determine if there is no remainder.
    if number % item == 0:
      # If there is no remainder the flag is switched to False from the True statement above.
      is_prime = False
  # Use an if statement so if the variable is_prime is indeed prime print it is prime.
  if is_prime:
    print("It's a prime number.")
  # Or if it's not prime print it's not prime.
  else:
    print("It's not a prime number.")

    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
# Stores the users chosen number.
n = int(input("Check this number: "))
# Calls the prime_checker function.
prime_checker(number=n)



