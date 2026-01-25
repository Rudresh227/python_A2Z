'''
LeetCode Problem: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note: Buying on day 2 and selling on day 3 would give profit = 4 - 1 = 3, which is less.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

'''


#My Approach

nums = [7,6,4,3,1]

left = 0
right = 1
maximum = 0

while right < len(nums):
    current = nums[right] - nums[left]
    maximum = max(current, maximum)

    if nums[right] < nums[left]:
        left = right

    right += 1

print(maximum)

#Optimal

prices = [7,6,4,3,1]

left = 0
max_profit = 0

for right in range(1, len(prices)):
    if prices[right] < prices[left]:
        left = right
    else:
        max_profit = max(max_profit, prices[right] - prices[left])

print(max_profit)


