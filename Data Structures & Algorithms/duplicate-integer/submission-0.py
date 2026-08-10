class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        box = []
        for item in nums:
            if item in box:
                return True
            box.append(item)
        return False
        