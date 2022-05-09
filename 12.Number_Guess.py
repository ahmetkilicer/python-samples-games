import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \   / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
EASY_LIVES = 10
HARD_LIVES = 5

#Kullanıcının girdiği değeri karşılaştıran ve yüksek alçak veya bildin sonucu veren fonksiyon
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Ur guess is high.")
    return turns - 1
  elif guess < answer:
    print("Ur guess is low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#oyuncunun kolay veya zor seçimini göre kullanacağı can sayısını döndürür
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LIVES
  else:
    return HARD_LIVES

def game():
  print(logo)
  #1-100 arasında rastgele sayı belirliyoruz
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)

  turns = set_difficulty()
  guess = 0
  #tahmin cevaba eşit olana kadar döngü devam ediyor
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #kullanıcıya tahmin yaptırıyoruz
    guess = int(input("Make a guess: "))

    #tahmini kontrol ediyoruz
    turns = check_answer(guess, answer, turns)
    #can biterse oyunu sonlandırıyoruz
    if turns == 0:
      print("You've run out of guesses, you lose.")
      break
    elif guess != answer:
      print("Guess again.")

while True:
  game()
  again=input("Do u wanna play again? yes or no: ")
  if again!="yes":
    break
  import os
  os.system('cls')