import tkinter as tk
from tkinter import messagebox
import random
import time


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.words_to_type = self.generate_random_words(10)
        self.current_word_index = 0
        self.num_correct_words = 0
        self.start_time = None

        self.label = tk.Label(root, text="Type the following words:", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.word_label = tk.Label(root, text=self.words_to_type[self.current_word_index], font=("Helvetica", 16))
        self.word_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.pack(pady=10)
        self.entry.focus_set()

        self.start_button = tk.Button(root, text="Start", command=self.start_typing_test)
        self.start_button.pack(pady=10)

    def generate_random_words(self, num_words):
        """Generate a list of random words for typing practice."""
        word_list = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "strawberry", "blueberry", "watermelon"]
        return random.choices(word_list, k=num_words)

    def start_typing_test(self):
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.entry.bind("<Return>", self.check_word)

    def check_word(self, event):
        user_input = self.entry.get().strip().lower()
        correct_word = self.words_to_type[self.current_word_index]

        if user_input == correct_word:
            self.num_correct_words += 1

        self.current_word_index += 1
        self.entry.delete(0, tk.END)

        if self.current_word_index < len(self.words_to_type):
            self.word_label.config(text=self.words_to_type[self.current_word_index])
        else:
            self.end_typing_test()

    def end_typing_test(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        wpm = self.calculate_wpm(elapsed_time)

        messagebox.showinfo("Typing Speed", f"Your typing speed is: {wpm:.2f} words per minute")
        self.reset_game()

    def calculate_wpm(self, elapsed_time):
        """Calculate words per minute (WPM)."""
        num_words = len(self.words_to_type)
        seconds_per_word = elapsed_time / num_words
        return 60 / seconds_per_word

    def reset_game(self):
        self.words_to_type = self.generate_random_words(10)
        self.current_word_index = 0
        self.num_correct_words = 0
        self.start_time = None
        self.word_label.config(text=self.words_to_type[self.current_word_index])
        self.entry.bind("<Return>", self.check_word)
        self.start_button.config(state=tk.NORMAL)
        self.entry.focus_set()


def main():
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    
