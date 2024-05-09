#This part of the code is so we have a function that makes sure the user gives us valid input for our problem
def userinput():
    while True:
        try:
            number = int(input("Enter the maximum value to check primes up to: "))
            if number >= 2:
                return number
        except ValueError:
            pass

#This part of the code is so we have a function that helps us find the prime using the definition of primes in the directions
def get_primes(max_num):
    primes = []
    for num in range(2, max_num + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

#This part of the code is just so we can print out the results of the the problem to the user
max_value = userinput()
prime_numbers = get_primes(max_value)
print(f"The primes from 2 to {max_value} are: {', '.join(map(str, prime_numbers))}")

