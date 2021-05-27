+ [House Robber](#ems/house-robber)
+ [House Robber II](#ems/house-robber-ii)
<!-----solution----->

## House Robber II

    https://leetcode.com/problems/house-robber-ii/

```python
    def robber_1(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
            # [rob1, rob2, n, n+1, ...]
        return rob2

    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(self.robber_1(nums[:-1]), self.robber_1(nums[1:]))
```

## House Robber

    https://leetcode.com/problems/house-robber/

```python
def rob(nums):
    rob1, rob2 = 0, 0
    for num in nums:
        newRob = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = newRob
        # [rob1, rob2, n, n+1, ...]
    return rob2



```