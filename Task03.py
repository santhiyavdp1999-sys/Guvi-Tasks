# 1. Guess the Number

import random
num=int(input("Guess the Number: "))
sys_gen_num=random.randint(1,10)
print("System Generated Number is " +str(sys_gen_num))
if (num==sys_gen_num):
    print("Great! You have find the exact match")
else:
    print("Better Luck, Next Time")

# 2. word scramble


import random
word=['python' , 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']
def play_word_scramble():
    original_word = random.choice(word)
    char_list = random.sample(original_word,len(original_word))
    scrambled_word = "".join(char_list)
    print("---Welcome to word scramble! ---")
    print(f"Scrambled word: {scrambled_word}")
    attempts=0
    while True:
        guess = input("Your guess:").strip().lower()
        attempts +=1
        if guess == original_word:
            print(f"Correct! you got it in {attempts} attempts.")
            break
        else:
            print("Wrong guess.Try again!")
if __name__ == "__main__":
    play_word_scramble()







