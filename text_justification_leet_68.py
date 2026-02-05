class WordAndFollowingSpaces():
    def __init__(self, wordString) -> None:
        self.wordString = wordString
        self.number_of_spaces_to_add = 1
    
    def build(self):
        return self.wordString + self.number_of_spaces_to_add * ' '

    def size(self):
        return len(self.wordString) + self.number_of_spaces_to_add

class Line:
    def __init__(self) -> None:
        self.words = []

    def stretch(self, max_width):
        pass

    def size(self):
        return sum(w.size() for w in self.words)


def stretch_line(line : Line, max_width):
    result = ""
    number_of_spaces_to_add = max_width - line.size()
    print(f"number_of_spaces_to_add {number_of_spaces_to_add}")
    return result

def build_line(words, current_index, max_width):
    word_next_index = current_index
    line = Line()
    while line.size() < max_width and word_next_index < len(words):
        preview_size = len(words[word_next_index]) + line.size()
        if preview_size > max_width:
            print("Biiiig ", preview_size)
            break
        else:
            line.words.append(WordAndFollowingSpaces(words[word_next_index]))
            word_next_index += 1
    return stretch_line(line, max_width), word_next_index

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
