class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = nums.count(val)
        for i in range(0,c):
            nums.remove(val)
        return len(nums)
