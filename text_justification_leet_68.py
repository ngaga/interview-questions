from math import floor

def justify(words, maxWidth):
    result = []
    for w in words:
        remaining_spaces = maxWidth - len(w)
        d_left = floor(remaining_spaces / 2)
        d_right = d_left
        if remaining_spaces % 2 != 0:
            d_left = d_left + 1
        print(d_left, d_right)
        line = ' ' * d_left + w + ' ' * d_right
        result.append(line)
    return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

justified = justify(words, maxWidth)
print(*justified, sep='|\n')

