class Solution:
    def find(self, left, right, val,arr):
        l = left
        r = right
        res = -1
        while l <= r:
            m = int((l + r) / 2)
            if arr[m] < val:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        n = len(nums);
        for i in range(n):
            for j in range(i+1,n-1):
                if i!=0 and nums[i] == nums[i-1]:
                    continue
                if j!=n-2 and nums[j] == nums[j+1] and nums[j] != nums[j+2]:
                    pass

                else:
                    if j != n-2:
                        if j != n - 2 and j - 1 == i and nums[j] == nums[j + 1]:
                            continue
                        if nums[j] == nums[j - 1] and j - 1 != i:
                            continue
                    else:
                        pass
               # if j == 2:
                #    print(i)
                c = -(nums[i]+nums[j])
                if nums[i+1] > c:
                    continue
                id = self.find(j+1,n-1,c,nums)
                if id != -1 and nums[id] == c:
                    print(i)
                    print(j)
                    ans.append([nums[i], nums[j], nums[id]])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-2,0,1,1,2]))
    print(sol.threeSum([0,0,0,0]))
    print(sol.threeSum([-1,0,0,1]))



