def rotate(nums, k):
    print(nums)
    l = len(nums)
    rotated = [0] * l
    print(rotated)
    for i, e in enumerate(nums):
        new_index = (i +  k) % l
        print(f"i, k, l {i}, {k}, {l}")
        print(f"new_index {new_index}")
        rotated[new_index] = e
    nums[:] = rotated
    print(nums)


nums = [1,2,3,4,5,6,7]
k = 3

rotate(nums, k)


# Output: [5,6,7,1,2,3,4]
