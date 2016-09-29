length = 0
word_not20 = 0
word20 = 0
total_words = 0

fin = open('word.txt')

for line in fin:
    word = line.strip()
    total_words += 1
    length = len(word)
    if length > 20:
        print word
        word20 += 1
    else:
        word_not20 += 1
print('\nTotal number of words in file: ' + str(total_words))
print('\nTotal words greater than 20 characters: ' + str(word20))
print('\nTotal words in file less than or equal to 20 characters: ' + str(word_not20))
