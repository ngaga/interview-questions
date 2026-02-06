def remove_dupplicates(nums):
    if len(nums) < 2:
        return len(nums)
    write_index = 1
    dupplicate_index = 1
    previous_value = nums[0] 
    while dupplicate_index < len(nums):
        if nums[dupplicate_index] == previous_value:
            pass
        else:
            nums[write_index] = nums[dupplicate_index]
            write_index += 1
            previous_value  = nums[dupplicate_index]
        dupplicate_index += 1
    return write_index


# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_dupplicates(nums))
print(nums)

