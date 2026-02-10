
def is_palindrom(s):
    def is_lower_alpha_numeric_string_palindrom(s):
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            if s[left_index] != s[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True

    lower_alpha_string = ""
    for element in s:
        if element.isalnum():
            lower_alpha_string += element.lower()
    print(lower_alpha_string)
    return is_lower_alpha_numeric_string_palindrom(lower_alpha_string)


s = "P0"
print(is_palindrom(s))
