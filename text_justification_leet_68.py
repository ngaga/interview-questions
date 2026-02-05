class LineElement():
    pass

class WordAndFollowingSpaces(LineElement):
    def __init__(self, wordString) -> None:
        self.wordString = wordString
        self.number_of_spaces_to_add = 1
    
    def build(self) -> str:
        return self.wordString + self.number_of_spaces_to_add * ' '

    def size(self):
        return len(self.wordString) + self.number_of_spaces_to_add

class Line:
    def __init__(self) -> None:
        self.words = []

    def stretch(self, max_width):
        number_of_spaces_to_add = max_width - self.size()
        word_count = len(self.words)
        print(f"number_of_spaces_to_add {number_of_spaces_to_add}, word_count: {word_count}")
        if word_count == 1:
            self.words[0].number_of_spaces_to_add = number_of_spaces_to_add
        else:
            # If n words there are n-1 spaces in between.
            interval_count = word_count - 1
            minimum_of_spaces_per_separation = 1 + number_of_spaces_to_add // interval_count
            remaining_spaces_to_place = number_of_spaces_to_add % interval_count
            print("quotien, reste ", minimum_of_spaces_per_separation, remaining_spaces_to_place)
            for w in self.words:
                w.number_of_spaces_to_add = minimum_of_spaces_per_separation
            self.clean_last_space()
            for i in range(remaining_spaces_to_place):
                self.words[i].number_of_spaces_to_add += 1

    def clean_last_space(self):
        self.words[-1].number_of_spaces_to_add = 0        

    def size(self):
        return sum(w.size() for w in self.words)

    def build(self) -> str:
        return ''.join([w.build() for w in self.words])

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
    line.clean_last_space()
    line.stretch(max_width)
    return line, word_next_index

def justify(words, max_width):
    result = []
    i = 0
    while i < len(words):
        line , i = build_line(words, i, max_width)
        print(f"line.size() {line.size()}")
        result.append(line.build())
    return result


# words = ["This", "is", "an", "example", "of", "text", "justification."]
# words = ["What","must","be","acknowledgment","shall","be"]
# max_width = 16
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
max_width = 20

justified = justify(words, max_width)
print(*justified, sep='|\n')
