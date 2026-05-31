class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_total = 0
        ans = []
        for num in nums:
            running_total += num
            ans.append(running_total)
        return ans