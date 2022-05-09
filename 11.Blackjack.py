#---------------------------------------BASİT BLACKJACK OYUNU----------------------------
#random modülü import ve logonun ascıı şeklinde yazılması 
import random
blackjacklogo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

#Oyun tekrar oynabilmesi için while loopuna sokuyoruz
again="y"
while again=="y":
  again=input("\nDo u wanna play Blackjack? \nType 'y' for yes, any button for no: ")
  #oynamak isdeğinde ekranı temizliyoruz
  if again=="y":
    import os
    os.system("cls")
  print(blackjacklogo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  #oyuncu ve bilgisayar için 2 adet rastgele kart seçiyoruz
  computer_cards=random.sample(cards,2)
  user_cards=random.sample(cards,2)
  #kartların toplamını döndüren fonksiyon
  def toplam(list):
    return sum(list)
  total_number= toplam(user_cards)

  print(f"Your cards are {user_cards[0]} and {+user_cards[1]}\nTotal number: {total_number}")
  print(f"Dealer first card is {computer_cards[0]}")

  #oyuncunun tekrar kart alabilmesi için kart istemeyene kadar tekrar eden while loopunu oluşturuyoruz
  while True:
    position=input("Do yu wanna hit or stand?\n(h for hit - s for stand): ").lower()
    #eğer hit der ise tekrar kart seçerek listeye ekliyoruz ve toplamıyla beraber kartları yazdırıyoruz
    if position=="h":
      new=random.choice(cards)
      user_cards.append(new)
      total_number=toplam(user_cards)
      #Eğer kart toplamı 21 den fazla ve içinde 11 var ise 11i 1 ile değiştiriyoruz (oyun kuralı)
      if 11 in user_cards and total_number>21:
        total_number-=10
      print("Your cards are " + ', '.join(map(str,user_cards)) + "\nYour total number is " +     str(total_number))
      if total_number>21:
        print("You lose!")
        break
      continue
    #kart istemez ise bilgisayarın destesini gösteriyoruz
    else:
      total_number_c=toplam(computer_cards)
      print("Dealer cards are " + ', '.join(map(str,computer_cards)) + "\nDealers total number is " +     str(total_number_c))

      #bilgisayarın eli 16 nın üzerine çıkana kadar kart çektiriyoruz
      while total_number_c<16:
        print("Dealer hit again!")
        new=random.choice(cards)
        computer_cards.append(new)
        total_number_c=toplam(computer_cards)
        if 11 in computer_cards and total_number_c>21:
          total_number_c-=10
        print("Dealer cards are " + ', '.join(map(str,computer_cards)) + "\nDealers total number is " +     str(total_number_c))
      #desteleri karşılaştırıp oyun sonucunu belirtiyoruz
      if total_number_c>21:
        print("You Win")
      elif total_number>total_number_c:
        print("You Win!")
      elif total_number==total_number_c:
        print("It-s a Tie!")
      else:
        print("Delaers Win, You lose!")
      break
          