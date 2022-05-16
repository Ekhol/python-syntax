def print_upper_words(words, must_start_with):
    for word in words:
        for letters in must_start_with:
            if word.startswith(letters):
                print(f"{word.upper()}")
