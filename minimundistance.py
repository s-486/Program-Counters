class Solution:
   def solve(self, nums):
   ans = 0
   seen = [False] * len(nums)
   for i, n in enumerate(nums):
      if not seen[i]:
         seen[i] = True
         ans += 1
         prev = n
   for j in range(i+1, len(nums)):
      if nums[j] > prev and not seen[j]: seen[j] = True
         prev = nums[j]
   return ans
ob = Solution()
nums = [1, 2, 7, 9, 3, 4]
print(ob.solve(nums))
