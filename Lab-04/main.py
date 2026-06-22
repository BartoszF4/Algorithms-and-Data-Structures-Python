from huffman import encode_huffman
from spell_checker import SpellChecker


def main():
    text = "I love data structures"
    encoded_text, codes, ratio = encode_huffman(text)

    print("Exercise 2:")
    print(f"Original: {text}")
    print(f"Encoded: {encoded_text}")
    for char, code in codes.items():
        print(f"'{char}': {code}")
    print(f"Compression Ratio: {ratio:.2f}\n")

    print("Exercise 1:")
    checker = SpellChecker('words_alpha.txt')
    checker.correct_file('input.txt', 'output.txt')
    print("Spelling correction completed. Check output.txt file.")


if __name__ == "__main__":
    main()