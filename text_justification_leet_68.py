

def build_line(words, current_index, max_width):
    word_next_index = current_index
    line = ""
    while len(line) < max_width and word_next_index < len(words):
        preview_size = len(words[word_next_index]) + len(line)
        if preview_size > max_width:
            print("Biiiig ", preview_size)
            break
        else:
            line += words[word_next_index]
            line += " "
            word_next_index += 1
    return line, word_next_index

def justify(words, max_width):
    result = []
    i = 0
    while i < len(words):
        line , i = build_line(words, i, max_width)
        print(f"len(line) {len(line)}")
        result.append(line)
    return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 16

justified = justify(words, max_width)
print(*justified, sep='|\n')


