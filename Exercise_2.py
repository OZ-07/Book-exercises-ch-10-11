"""still chapter 10"""
from exercise_1 import value_counts

""
def find_duplicates(word):
    print(value_counts(word))
    return len(value_counts(word).values())!= len(word)

def has_duplicates(word):
    return len(set(word)) != len(word)

def main():
    print(find_duplicates('subdermatoglyphic'))
    print(find_duplicates('hello'))

if __name__ == '__main__':
    main()