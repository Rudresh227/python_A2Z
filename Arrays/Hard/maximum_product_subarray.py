# Leetcode: https://leetcode.com/problems/maximum-product-subarray/submissions/1463069552/

nums = [2,3,-2,4]
max_prod = float('-inf')  # Initialize to smallest possible value

current_prod = 1
# Forward pass
for num in nums:
    current_prod *= num 
    max_prod = max(max_prod, current_prod)
    if current_prod == 0:  # Reset if zero encountered
        current_prod = 1

    # Backward pass
current_prod = 1
for num in reversed(nums):
    current_prod *= num
    max_prod = max(max_prod, current_prod)
    if current_prod == 0:  # Reset if zero encountered
        current_prod = 1

print(max_prod)
