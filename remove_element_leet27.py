def remove_value(numbers, value_to_remove):
    move_index = 0
    write_index = len(numbers) - 1
    remove_count = 0
    while move_index != write_index:
        if numbers[write_index] == value_to_remove:
            numbers[write_index] = -1
            write_index -= 1
            remove_count += 1
            continue
        if numbers[move_index] != value_to_remove:
            move_index +=1
            continue
        else:
            numbers[move_index], numbers[write_index] = numbers[write_index], -1
            remove_count += 1
            write_index -= 1
            move_index += 1
    return remove_count


# nums = [3,2,2,3]
# val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_value(nums, val))
print(nums)
