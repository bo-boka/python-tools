letter_counts = {}
for letter in 'missippi':
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
# .get() function parameter takes key and default none/0 etc if there's no value
print letter_counts