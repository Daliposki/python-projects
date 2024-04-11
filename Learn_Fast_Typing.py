import random
import time


def generate_random_words(num_words):
    """Generate a list of random words for typing practice."""
    word_list = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "strawberry", "blueberry", "watermelon"]
    return random.choices(word_list, k=num_words)


def get_user_input():
    """Get user input for typing."""
    return input("Type the word: ")


def calculate_wpm(num_correct_words, elapsed_time):
    """Calculate words per minute (WPM)."""
    seconds_per_word = elapsed_time / num_correct_words
    return 60 / seconds_per_word


def main():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start...")

    num_words = 10  # Number of words for the typing test
    words_to_type = generate_random_words(num_words)
    print("Type the following words:")
    print(" ".join(words_to_type))

    start_time = time.time()
    num_correct_words = 0
    for word in words_to_type:
        user_input = get_user_input()
        if user_input == word:
            num_correct_words += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    wpm = calculate_wpm(num_correct_words, elapsed_time)
    print(f"Your typing speed is: {wpm:.2f} words per minute")


if __name__ == "__main__":
    main()
