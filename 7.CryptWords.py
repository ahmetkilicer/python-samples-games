#KRİPTOLAMA İŞLEMİNDE KULLANICAĞAMIZ ALFABE
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#############################################################################################################################333
#                                                       FONKSİYONLAR
#                       (FONKSİYONLARA BAKMADAN ÖNCE ALTTAKİ KODU OKURSANIZ DAHA AÇIKLAYICI OLUR.)


#kripto işlemini yapan fonksiyonu tanımladık
def encrypt(text,shift):
  #kriptonun son halinin yazılacağı boş bir string oluşturduk
  text_new=""
  #verilen kelimenin her harfi için for loopuna sokuyoruz
  for i in range(len(text)):
    #inputta bulunan eleman harf ise kripto işlemini yapacak, değlse aynı şekilde bırakacak bir if else statementi yazdık. 
    if text[i] in alphabet:
      #ilk harfin alfabedeki pozisyonunu buluyoruz, for loopu sayesinde her harf için gerçekletiricez bu süreci
      letter=alphabet.index(text[i])
      #kaydırmak istediği rakam alfabeden büyükse modülüs ünü alıp kalan sayıyı buluyoruz///alfabe 26 harfli(ingilizce) 27 defa kaydırmak istemesi aslında 1 defa kaydırmak istemesi demek, bu yüzden modülüs aldık
      shift=shift%len(alphabet)
      #yeni harfimizin pozisyonu= eski pozisyon+kaydırma sayısı
      position=letter+shift
      # eğer z harfini seçerse bu konumda pozisyonu 25 oluyor(len=26 olduğunu düşünürsek), 2 kere kaydırmak istese 
      # b harfini elde etmemiz lazım. Fakat pozisyon 25+2=27 oluyor alfabe indexsinden fazla yani, bu yüzden 27-len(alphabet) yaparak 27-26=1 elde ediyoruz ve alphabet[1]=b harfi olduğundan işlemimiz tamamlanıyor.
      if (position)>(len(alphabet)-1):
        position=position-(len(alphabet))
      #Her harfi text_new stringimize ekliyoruz ve kriptolu halini buluyoruz
      text_new+=alphabet[position]
      #ve Yazdırıyoruz

    #Eğer harf değilde rakam veya sembol var ise kripto işlemine sokmadan direk text'imizin son haline ekliyor.
    else:
      text_new+=text[i]
  print(f"The encoded text is {text_new}")


#Alttaki fonksiyonda decrypt işlemi için, tüm süreç aynı aslında sadeve bu sefer kaydırma sayısını poziyondan çıkartıyoruz , alfabe tersten -1 pozisyonundan başladığı için yukarıdaki gibi ekstra bir işlem yapmıyoruz. Daha kolay yani.
def decrypt(text,shift):
  text_new=""
  for i in range(len(text)):
    if text[i] in alphabet:
      letter=alphabet.index(text[i])
      shift=shift%len(alphabet)
      position=letter-shift
      text_new+=alphabet[position]
    else:
      text_new+=text[i]
  print(f"The decoded text is {text_new}")


#                                             YUKARIDA FONKSİYONLAR TANIMLANMIŞTIR
#########################################################################################################################################




#Proramın sürekli çalışması için while true loop una soktuk
end=True
while end:
  #Kullanıcının kriptolamamı yoksa tersinimi yaptığını öğreniyoruz
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

  #Kullanıcı encode yada decode dışında bir giriş yaparsa diye  if statement ı koyduk, yanlış girişte while loop unun başına gönderiyor.
  if direction!="encode" and direction!="decode":
      print("Yanlış bir giriş yaptınız, Lütfen tekrar deneyiniz!!!")
      continue
  #Kullanıcıdan kriptolanacak kelimeyi aldık ve tüm harflerini küçülttük, çünkü elimizdeki alfabe listesi hep küçük harften oluşuyor
  text = input("Type your message:\n").lower()

  #Kaç harf kaydırıp kripto yapmamızı veya çözmemizi istediğini soruyoruz.
  shift = int(input("Type the shift number:\n"))
  
  #Kullanıcı girişlerine göre yazdığımız fonksiyonları çağırıyoruz.
  if direction=="encode":
    encrypt(text,shift)
  elif direction=="decode":
    decrypt(text,shift)

  again=input("Do u wanna try again?(yes or no): ").lower()
  if again=="yes":
    end=True
  else:
    print("Thank u!")
    end=False
