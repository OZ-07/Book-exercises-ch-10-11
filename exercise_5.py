# from exercise_1 import value_counts

def load_word_dict(file_path):
    word_dict = {}
    with open(file_path,'r') as word_file:
        for word in word_file:
            word = word.strip().lower()
            word_dict[word] = True
    return word_dict



def is_interlocking(word,word_dict):
    word = word.lower()
    first = word [0::2]
    second = word[1::2]
    return first in word_dict and second in word_dict

def main():
    print(is_interlocking('schooled', load_word_dict('Word library/words.txt')))
    word = 'schooled'

if __name__ == '__main__':
    main()