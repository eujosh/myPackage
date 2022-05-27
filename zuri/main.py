# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file = open('story.txt')
    text = file.read()
    return text


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    word_count = {}

    word_split = text.split()
    for word in word_split:
        word_count[word] = word_split.count(word)

    return word_count

word_count = count_words()
print(word_count)
