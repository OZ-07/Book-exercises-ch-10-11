from exercise_1 import value_counts


def most_frequent_letters(string):
    counter = {}
    for letter in string:
        counter[letter]  = counter.get(letter, 0) +1
    return sorted(counter,Reverse=True)




def main():
    print(value_counts('hello'))
    # h:1,e:1,l:2,o:1

if __name__ == '__main__':
    main()