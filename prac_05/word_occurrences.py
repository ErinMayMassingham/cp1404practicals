""" word occurrences
Estimate : 20 minutes
Actual: 30 minutes """

words_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    words_to_count[word] = words_to_count.get(word, 0) + 1

sorted_words = sorted(words_to_count.keys())

max_length = max((len(word) for word in sorted_words))
for word in sorted_words:
    print(f"{word:{max_length}} : {words_to_count[word]}")
