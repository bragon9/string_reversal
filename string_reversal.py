import argparse


def init_args():
    """Add parser and arguments."""
    parser = argparse.ArgumentParser(
        description="Given a file name, reverses the string contained within \
                    the file."
    )
    parser.add_argument(
        "filename",
        type=str,
        help="The filename containing the string to reverse.",
    )
    parser.add_argument(
        "-r",
        dest="reverse_letters",
        action="store_true",
        help="Reverses the string letter for letter.",
    )
    parser.add_argument(
        "-w",
        dest="reverse_words",
        action="store_true",
        help="Reverses the string word for word.",
    )
    return parser.parse_args()


def get_string_from_file(path):
    """Return the string in the given file."""
    with open(path) as file:
        return file.readline()


def reverse_string(s):
    """Reverse a string by letters."""
    return s[::-1]


def reverse_words(s):
    """Reverse a string by words."""
    return " ".join([reverse_string(word) for word in s.split(" ")])


if __name__ == "__main__":
    args = init_args()

    reverse_letters_bool = args.reverse_letters
    reverse_words_bool = args.reverse_words
    filename = args.filename

    input_str = get_string_from_file(filename)

    # Only allow one flag
    if reverse_letters_bool and reverse_words_bool:
        raise ValueError('Only one flag may be used at a time.')

    if reverse_letters_bool:
        print(reverse_string(input_str))

    if reverse_words_bool:
        print(reverse_words(input_str))
