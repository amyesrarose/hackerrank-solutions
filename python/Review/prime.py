def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # Check for factors from 2 up to n-1
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a factor, so it's not prime
            
    return True  # If no factors were found, it's prime

print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False