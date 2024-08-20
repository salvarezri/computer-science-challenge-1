class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_zero = 0
        index_none_zero = 1
        while index_none_zero < len(nums) and index_zero < len(nums):
            # find a zero
            if nums[index_zero] == 0:
                if nums[index_none_zero] != 0:
                    # Exchange values
                    nums[index_zero] = nums[index_none_zero]
                    nums[index_none_zero] = 0
                    index_zero += 1
                    index_none_zero += 1
                else:
                    # Finde the next no-zero value
                    index_none_zero += 1
            else:
                # update zero pointer
                if index_none_zero <= index_zero:
                    index_none_zero = index_zero+1
                else:
                    index_zero += 1