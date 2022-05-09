#random modülünün importu
import random
#Alfabe,numara ve sembol listeleri
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#kullanıcıdan kaç tane harf sembol ve numara istediğinin öğrenilmesi
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#üç adet string oluşturuyoruz
pass_letters,pass_symbols,pass_numbers="","",""

letters_len=len(letters)
symbols_len=len(symbols)
numbers_len=len(numbers)
#her listeden rastgele istenen adet kadar eleman şeçilmesi ve boş listelere eklenmesi, choice() ilede yapılabilir(daha kısa)
for i in range(0,nr_letters):
  j=random.randint(0,letters_len-1)
  pass_letters+=letters[j]
for i in range(0,nr_symbols):
  j=random.randint(0,symbols_len-1)
  pass_symbols+=symbols[j]
for i in range(0,nr_numbers):
  j=random.randint(0,numbers_len-1)
  pass_numbers+=numbers[j]

#eklenen elemanların birleştirilmesi ve karıştırılması
s=pass_letters+pass_symbols+pass_numbers
password_end=''.join(random.sample(s,len(s)))

#print(s)
print(password_end)
