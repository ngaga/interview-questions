def merge(nums1, m: int, nums2, n: int) -> None:
    i, j = m - 1, n - 1
    writing_index = n + m - 1
    while i >= 0 and j >= 0:
        print(f"i, j {i}, {j}")
        print(f"nums1[i] {nums1[i]}, nums2[j] {nums2[j]}")
        if nums1[i] >= nums2[j]:
            nums1[writing_index] = nums1[i]
            i -= 1
            writing_index -=1
        else:
            nums1[writing_index] = nums2[j]
            j -= 1
            writing_index -= 1
        print(f"nums1 {nums1}, nums2 {nums2}")
    while j >= 0:
        nums1[writing_index] = nums2[j]
        j -= 1
        writing_index -= 1
    while i >= 0:
        nums1[writing_index] = nums1[i]
        i -= 1
        writing_index -= 1


def merge2(nums1, m: int, nums2, n: int):
    result = []
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    while i < m:
        result.append(nums1[i])
        i += 1
    while j < n:
        result.append(nums2[j])
        j += 1
    nums1[:] = result



nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)
