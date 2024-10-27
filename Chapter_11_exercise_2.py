"""
We can use letter_map and letters to encode and decode words using a Caesar cipher.
A Caesar cipher is a weak form of encryption that involves shifting each
letter by a fixed number of places in the alphabet,
wrapping around to the beginning if necessary.
For example, 'a' shifted by 2 is 'c' and 'z' shifted by 1 is 'a'.
Write a function called shift_word that takes as parameters a string and an integer,
and returns a new string that contains
the letters from the string shifted by the given number of places.

"""


letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

"""def shift_word(word,shift):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_map = {letter:index for index, letter in enumerate(letters)}
    shifted_word = ""
    for char in word:
        if char.isalpha():
            lowerchar= char.lower
            original_index=letter_map[lowerchar]
            new_index = (original_index + shift) % 26
            shifted_char = letters[new_index]
        else:
            shifted_word += char
    return shifted_word
""" """this is pretty much what I could get out of chat GPT and it doesn't make any sense"""
def shift_word(word,shift):
    letter_map('word','shift')




def main():
    print(shift_word('cheer',7))  # should be jolly



if __name__ == '__main__':
    main()