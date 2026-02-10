from math import floor


def product_but_one(nums):
    full_product = 1
    zero_count = nums.count(0)
    for n in nums:
        if n != 0:
            full_product *= n
    if zero_count > 1:
        return [0] * len(nums)
    elif zero_count == 1:
        return [full_product if n == 0 else 0 for n in nums]
    result = [full_product] * len(nums)
    for i, n in enumerate(nums):
        result[i] //= n
    return result

nums = [1,2,3,4]
# Output: [24,12,8,6]

# nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

print(product_but_one(nums))
