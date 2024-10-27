def solve_test_case():
    N = input().strip()  # Keep as string
    n = len(N)
    
    if n < 3:
        return "Kamu"  # First player can't make a move
    
    # Pre-compute which windows are divisible by 3
    divisible = [False] * (n-2)
    for i in range(n-2):
        num = int(N[i:i+3])  # Get the actual 3-digit number
        divisible[i] = (num % 3 == 0)
    
    # dp[i] represents whether the player facing string length i wins
    dp = [False] * (n + 1)
    
    # Base cases
    dp[0] = dp[1] = dp[2] = False  # Can't make a move with less than 3 digits
    
    # Fill dp
    for length in range(3, n + 1):
        # For current length, check if any move leads to a losing position for opponent
        can_win = False
        
        # Number of 3-digit windows possible with current length
        windows = length - 2
        
        # Check each possible starting position for a 3-digit window
        for i in range(windows):
            # If this window is divisible by 3
            if divisible[i]:
                # After removing middle digit, opponent faces length-1
                if not dp[length - 1]:
                    can_win = True
                    break
        
        dp[length] = can_win
    
    return "Anda" if dp[n] else "Kamu"

# Handle multiple test cases
T = int(input())
for _ in range(T):
    result = solve_test_case()
    print(result)