def rotate(nums, k):
   def reverse_between_indexes(nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    l = len(nums)
    k = k % l
    reverse_between_indexes(nums,0 , l - 1)
    reverse_between_indexes(nums, 0, k - 1)
    reverse_between_indexes(nums, k, l - 1)
    


nums = [-1]
k = 2

rotate(nums, k)

print(nums)
