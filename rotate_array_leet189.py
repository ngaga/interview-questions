def rotate(nums, k):
    def reverse_between_indexes(nums, i, j):
        while i < j:
            try:
                nums[i], nums[j] = nums[j], nums[i]
            except:
                print(f"error: i, j {i} {j}")
                return
            i += 1
            j -= 1

    l = len(nums)
    reverse_between_indexes(nums, 0 , l - 1)
    print(f" l - 1, nums {l -1} {nums}")
    reverse_between_indexes(nums, 0, k - 1)
    print(nums)
    reverse_between_indexes(nums, k, l - 1)
    print(nums)


nums = [-1]
k = 2

rotate(nums, k)

print(nums)
