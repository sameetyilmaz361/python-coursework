a = "This is a test. This test is only a test.This is a test."


def count_words(text):


    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts            



from collections import Counter
def count_words_fast(text):


    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))

    return word_counts         




print(len(count_words("This comprehension check is to check for comprehension.")))
print(count_words(a) is count_words_fast(a))
