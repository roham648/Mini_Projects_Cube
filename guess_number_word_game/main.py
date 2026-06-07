import random
import json
import sys
import os

# --- حل مشکل نمایش فارسی در ویندوز ---
# این خطوط کد باعث میشه پایتون متن‌های فارسی رو درست نمایش بده
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')

# --- کلاس بازی کلمات (Word Game) ---
class WordGame:
    def __init__(self, language):
        self.language = language
        self.data = []
        self.load_data()

    def load_data(self):
        if self.language == "fa":
            # تلاش برای خواندن فایل با کدگذاری UTF-8
            try:
                with open("dataset_word_fa.json", "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except FileNotFoundError:
                print("خطا: فایل dataset_word_fa.json پیدا نشد. لطفاً فایل را در کنار main.py قرار دهید.")
                sys.exit()
            
            print("hint (all of categories are these): دور زمین, زینتی, خوراکی, مالی, اقامتی, عبادتگاه, مکان, حمل و نقل, پستاندار, تفریحی, کوهستان, جاندار, وسیله, بیمارستان, روستا, آسمان, مسکونی, مبلمان, غیر وحشی, نقلیه, شیرده, قمر, روشنایی, پشمی, ساختمانی, فرهنگی, درمانی, شی, لوازم خانگی, حیوان, میوه, نوشت‌افزار, عنصر, ورزشی, مدرسه, آموزشی, گیاه, ابزار, ستاره, طبیعت, شهر, بهداشت, مایع حیات, شغل, صنعتی, تعمیرات")
        elif self.language == "en":
            try:
                with open("dataset_word_en.json", "r", encoding="utf-8") as f:
                    self.data = json.load(f)
                print("hint (all categorise are these): ")
            except FileNotFoundError:
                print("خطا: فایل dataset_word_en.json پیدا نشد. لطفاً فایل را در کنار main.py قرار دهید.")
                sys.exit()
        else:
            print("Language not supported.")
            sys.exit()

    def game(self):
        random_dict = random.choice(self.data)
        word = random_dict["word"]
        category = random_dict["categories"]
        try:
            category_0 = category[0]
            try:
                category_1 = category[1]
                try:
                    category_2 = category[2]
                except:
                    category_2 = None
            except:
                category_1 = None
        except:
            category_0 = None
        for i in range(1, 1001):
            user_guess = input("your guess: ")
            if str(user_guess) == word:
                print("you won!!")
                break
            elif str(user_guess) == category_0:
                print("yes")
            elif str(user_guess) == category_1:
                print("yes")
            elif str(user_guess) == category_2:
                print("yes")
            else:
                print("no")
        end = input("do you want to restart?")
        if end == "yes":
            return self.game()

# --- کلاس بازی اعداد (Number Game) ---
class NumberGame:
    def game(self):
        need_list = []
        n_list = []
        random_number = random.randint(1, 1000)
        print("game normally generate number from 1 to 1000")
        need_list.append(random_number)
        
        for i in range(1, 100000):
            try:
                b = int(input("what is your guess:"))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if b < random_number:
                print("number is bigger")
                n_list.append(b)
            else:
                print("number is smaller")
                n_list.append(b)

            if len(n_list) >= 20:
                print("you ask more than 20")
                break
            elif b == random_number:
                print("you won!")
                break

        inp = input("do you want to restart? ")
        if inp == "yes":
            self.game()

# --- برنامه اصلی ---
if __name__ == "__main__":
    print("Welcome! Which game do you want to play?")
    print("1. Word Guessing Game")
    print("2. Number Guessing Game")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        lang = input("what language do you want to guess word (en or fa): ").strip()
        game_instance = WordGame(lang)
        game_instance.game()
    elif choice == "2":
        game_instance = NumberGame()
        game_instance.game()
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")
