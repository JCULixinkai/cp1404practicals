
def main():
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    print_word_counts(word_counts)

def count_word_occurrences(text):
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def print_word_counts(word_counts):
    max_length = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:{max_length}} : {word_counts[word]}")

    main()
