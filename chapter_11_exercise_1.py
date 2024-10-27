"""
Write a line of code that appends the value 6 to the end of the second list in t.
 If you display t, the result should be ([1, 2, 3], [4, 5, 6]).

Try to create a dictionary that maps from t to a string,
 and confirm that you get a TypeError.
"""

list_1 = ['1','2','3']
list_2 = ['4','5']

t = (list_1,list_2)

def add_tuples(list):
    list.append(6)
    return list




def main():
    print(list_1)
    print(add_tuples([t]))


if __name__ == '__main__':
    main()