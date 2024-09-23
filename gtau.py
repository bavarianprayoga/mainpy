# def sum_odd_numbers(n):
#     # Base case: if n is 0, return 0
#     if n == 0:
#         return 0
    
#     # Calculate the nth odd number
#     nth_odd = 2 * n - 1
    
#     # Recursive case: add the nth odd number to the sum of the first (n-1) odd numbers
#     return nth_odd + sum_odd_numbers(n - 1)

# # Example usage
# N = 20
# result = sum_odd_numbers(N)
# print(f"The sum of the first {N} odd numbers is: {result}")


def sum_of_odd_numbers(N):
    if N == 0:
        return 0
    else:
        return (2 * N - 1) + sum_of_odd_numbers(N - 1)

# Example usage
N = 20
print(sum_of_odd_numbers(N))  # Output should be 25 (1 + 3 + 5 + 7 + 9)