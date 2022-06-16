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
        split_word = no_punct.lower()#.replace(" ", "")
        new_list = split_word.split(' ')
        #print(new_list)

    def get_numbers(s, e, i):
        return list(range(s, e, i))
    start, end, intval = 1, 662, 1
    zip_list = zip(get_numbers(start, end, intval), new_list)
    print(zip_list)
    print(dict(zip_list))

#        print(f' "we" appears {new_list.count("we")} time(s)')

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
