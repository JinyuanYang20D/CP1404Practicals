def main():
    """Count the occurrences of words"""
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    max_length = max(len(word) for word in word_counts)
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_length}} : {count}")

text = input("Enter a string: ")
main()