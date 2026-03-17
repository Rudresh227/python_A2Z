class Solution:
    def solve(self, A, B):
        prefix = 0
        dict = {0: 1}
        count = 0

        for num in A:
            prefix ^= num

            target = prefix ^ B
            if target in dict:
                count += dict[target]

            if prefix not in dict:
                dict[prefix] = 1
            else:
                dict[prefix] += 1

        return count