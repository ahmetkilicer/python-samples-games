rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#random modülünün import edilmesi
import random

#kullanıcının rock,paper,scissors arasından seçim yapması
choose=int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors."))
#seçeneklerin liste içinde belirtilmesi (index numarasına göre)
options=[rock,paper,scissors]
#bilgisayarın rastgele bir seçim yapması
computer_number=random.randint(0,2)
computer_choose=options[computer_number]

#karşılaştırma ve sonuç gösterme kısmı
if choose>2:
  choose=choose%3
player_choose=options[choose]
print("\nYou chose:\n"+player_choose)
print("\nComputer chose:\n"+computer_choose)
if computer_choose!=player_choose:
  if computer_choose==rock and player_choose==scissors:
    print("Computer Win, You Lost!!!")
  elif computer_choose==rock and player_choose==paper:
    print("You Win, Congratulations!!!")
  elif computer_choose==paper and player_choose==scissors:
    print("You Win, Congratulations!!!")
  elif computer_choose==paper and player_choose==rock:
    print("Computer Win, You Lost!!!")
  elif computer_choose==scissors and player_choose==rock:
    print("You Win, Congratulations!!!")
  elif computer_choose==scissors and player_choose==paper:
    print("Computer Win, You Lost!!!")
    
else:
  print("It is a draw!")