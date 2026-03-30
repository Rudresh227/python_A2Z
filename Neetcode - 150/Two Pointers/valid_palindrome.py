#Solution - 1
s = "A man, a plan, a canal: Panama"
new_str = ""

for char in s:
    if char.isalnum():
        new_str += char.lower()

print(new_str == new_str[::-1])

#Solution - 2
s = "A man, a plan, a canal: Panama"

left = 0
right = len(s) - 1
flag = True

while left <= right:
    if not s[left].isalnum():
        left += 1
        continue
    if not s[right].isalnum():
        right -= 1
        continue

    if s[left].lower() != s[right].lower():
        flag = False
        break

    left += 1
    right -= 1

print('Flag:',flag)

#Solution - 3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l is the "left" pointer, r is the "right" pointer
        l, r = 0, len(s) - 1

        while l < r:
            # Skip characters that aren't letters or numbers from the left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Skip characters that aren't letters or numbers from the right
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # Compare the characters (ignoring capital letters)
            if s[l].lower() != s[r].lower():
                return False

            # Move both pointers toward the middle
            l += 1
            r -= 1

        return True

    def alphaNum(self, c):
        # Checks if a character is A-Z, a-z, or 0-9 using ASCII values
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


# --- Testing the function ---
sol = Solution()
example_input = "A man, a plan, a canal: Panama"
result = sol.isPalindrome(example_input)

print(f"Is the string '{example_input}' a palindrome? {result}")