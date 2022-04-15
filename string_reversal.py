import argparse


def init_args():
    """Add parser and arguments."""
    parser = argparse.ArgumentParser(description="Reverse a string.")
    parser.add_argument(
        "string",
        type=str,
        help="The string to reverse, wrapped in quotes (single or double).",
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
    input_str = args.string

    if reverse_letters_bool:
        print(reverse_string(input_str))

    if reverse_words_bool:
        print(reverse_words(input_str))
