import string

def get_sentence():
    """Ask the user for a valid sentence."""
    while True:
        sentence = input("Enter a sentence: ")
        
        if sentence and sentence[0].isupper() and sentence[-1] in ".!?":
            return sentence
        print("Please start with a capital letter and end with '.', '!' or '?'.")


def calculate_frequencies(sentence):
    """Count how many times each word appears."""
    words = []
    freqs = []
    for token in sentence.split():
        word = token.strip(string.punctuation).lower()
        if not word:
            continue
        if word in words:
            freqs[words.index(word)] += 1
        else:
            words.append(word)
            freqs.append(1)
    return words, freqs


def print_frequencies(words, freqs):
    """Print the words and their counts."""
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {freqs[i]}")


def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)


if __name__ == "__main__":
    main()
