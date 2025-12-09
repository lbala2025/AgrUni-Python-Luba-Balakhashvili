from functools import reduce

sentence = "Data Science is fun and Data Analysis is powerful if data is understood well."

# 1
words = sentence.replace(".", "").split()
print("Words:", words)

# 2
lower_words = list(map(lambda w: w.lower(), words))
print("\n Lowercase:", lower_words)

# 3
word_count = reduce(
    lambda acc, w: {**acc, w: acc.get(w, 0) + 1},
    lower_words,
    {}
)

print("\n Word count:\n", word_count)

# 4
mostly_used = max(word_count.items(), key=lambda x: x[1])
print("\n Mostly used word:", mostly_used)


