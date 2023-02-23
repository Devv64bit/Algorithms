class Solution:
    def findKthLargest(self, nums, k):
        # k is the index of the kth largest element in the array
        k = len(nums) - k

        def quickSelect(lhs, rhs):
            pivot, pointer = nums[rhs], lhs
            # for loop to iterate through the array
            for i in range(lhs, rhs):
                # if the current element is smaller than the pivot
                if nums[i] <= pivot:
                    # swap with the pointer index
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            # swap the pivot value with the pointer index
            nums[pointer], nums[rhs] = nums[rhs], nums[pointer]

            # k value less than pointer
            if pointer > k:
                # recursively call quickSelect on the left portion of the array
                # right pointer is shifted to the left
                return quickSelect(lhs, pointer - 1)
            elif pointer < k:
                # recursively call quickSelect on the right portion of the array
                # left pointer is shifted to the right
                return quickSelect(pointer + 1, rhs)
            else:
                # return the kth largest element
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums, k))
