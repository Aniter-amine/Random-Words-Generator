from random_word import RandomWords

r = RandomWords()

# Input To Define The Length Of The Random Word
inp = int(input('Enter The Length Of The Word: '))

# Return a single random word With The Length Of The Input
word = r.get_random_word(maxLength=inp)

# Printing The Random Word
print(word)
