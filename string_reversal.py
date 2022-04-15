def reverse_string(s):
    """Reverse a string by letters."""
    return s[::-1]


def reverse_words(s):
    """Reverse a string by words."""
    return " ".join([reverse_string(word) for word in s.split(" ")])


if __name__ == "__main__":
    input_str = input("Enter string to reverse\n")
    print(reverse_words(input_str))
