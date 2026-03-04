class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign
        sign = -1 if x < 0 else 1

        # Reverse the absolute value using string slicing
        reversed_num = int(str(abs(x))[::-1]) * sign

        # 32-bit signed integer overflow check
        if reversed_num < -2 ** 31 or reversed_num > 2 ** 31 - 1:
            return 0

        return reversed_num