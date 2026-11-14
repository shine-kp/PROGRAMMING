class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        out = float('inf')
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + nums[i - 1]

        for left in range(0, n - l + 1):
            for right in range(left + l, min(left + r, n) + 1):
                curSum = pref[right] - pref[left]
                if curSum > 0:
                    out = min(out, curSum)

        return out if out != float('inf') else -1