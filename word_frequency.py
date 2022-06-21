#from operator import truediv
#from optparse import Values
import pprint

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file. Your code goes here"""
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.read()
        no_punct = read_file.replace(",", "").replace(".", "").replace("?", "")
        #print(no_punct)
        new_list = no_punct.lower().split()
        no_stop_list = []
        for word in new_list:
            if word not in STOP_WORDS:
                no_stop_list.append(word)
        #print(new_list)

    make_dictionary = dict.fromkeys(no_stop_list, 0)
    for word in no_stop_list:
        make_dictionary[word] += 1
    #print(make_dictionary)
    dict_list = sorted(make_dictionary.items(), reverse=True, key=lambda x: x[1])
    sortdict = dict(dict_list)
    for word, count in sortdict.items():
        print(f"{word} | {count} {count*'*'}")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)