# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename, "r") as w:
        text = w.read()
    return text


def count_words():
    text = read_file_content("./story.txt")
    words = (text.split())
    unique_words = set(words)
    bible = {}
    for word in unique_words:
        bible.update({word: words.count(word)})
    return bible


count = count_words()
print(count)
