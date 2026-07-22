def read_book(title_path):
    """Reads a book from a file. Returns the book as a string."""

    with open(title_path, "r" , encoding="utf-8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text


def word_stats(word_counts):

    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)



