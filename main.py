import random
import time

words = ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig', 'grape', 'honeydew', 'iceberg', 'jackfruit','kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla', 'watermelon', 'xigua', 'yellowtail', 'zucchini', 'almond', 'broccoli','cauliflower', 'dill']


def generate_sentence():
    return " ".join(random.choices(words, k=10))

def wpm_measure(start_time, end_time, sentence):
    time_taken = end_time - start_time
    words_typed = len(sentence.split())
    wpm = int(words_typed / (time_taken / 60))
    return wpm

def test():
    print('Welcome to the Speed Typing Test!\n')
    input('Press Enter Key to start :')

    sentence = generate_sentence()
    print('\nType the following sentence:\n')
    print(sentence)

    start_time = time.time()
    user_input = input("\n>> ")
    end_time = time.time()

    wpm = wpm_measure(start_time, end_time, sentence)

    print(f'\nYour typing speed is : {wpm} WPM')
    print("Test is Over")

test()

