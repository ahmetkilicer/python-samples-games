#random modülü ve kullanacağım ASCII resimlerinin/logonun diğer dosyadan import edilmesi
import random
from asamalar import asamalar, logo
#Yine aynı şekilde kelime listesinin başka py dosyasından importu
from kelimeler import kelimeler

#kelime listesinden rastgele bir kelimenin seçilmesi
secilmis_kelime=random.choice(kelimeler)

#Aynı uzunlukta tüm karakterlerin "_" olduğu bir listenin oluşturulması
gorunen_kelime=[]
for i in secilmis_kelime:
    gorunen_kelime+="_"

#oyun başlangıcında logonun gözükmesi
print(logo)
print("\nADAM ASMACA OYUNUNA HOŞGELDİNİZ!!!")

#stages.py klasöründeki resimlerden en sondaki oyun başlangıç tahtasının resmi burada, onu çekiyorum
#oyuncunun 6 deneme hakkı var ve asamaların son resmi oyun başlangıç resmi, ilerde tahmin edilen harf seçilmiş kelime içinde olmadığında lives değişkeninini 1 azaltıcam ve aşamalar ilerlemiş olacak
lives=6
print(asamalar[lives])

#Tahmin ederken harf sayısı kadar "_" işareti gözüksün istiyorum,
#yukarıda gorunen_kelime isimli listeyi oluşturmuştuk,
#gorunen_kelime adlı listeyi aralarında bir boşluk ile stringe çevirip ekrana veriyorum daha düzgün gözüküyor.(join komutu ile)
#print(secilmis_kelime) <<<<<< burdaki komutu, oyunu yazarken ne yaptığımı görebileyim diye eklemiştim, oyun sonunda ihtiyacım kalmadı.
print(' '.join(gorunen_kelime))

#Sürekli tahmin etmeye devam etmesi için while döngüsüne soktuk, kullanıcanın canları tükendiğinde oyun_sonu değişkenini False yaparak oyun sonlandırıcaz.
oyun_sonu=True
while oyun_sonu:
    #Kullanıcıdan harf tahmin etmesini isteyerek değişkene atıyoruz ve kullanıcının büyük harf girme ihtimaline göre küçültüyoruz
    tahmin=input("\nBir harf tahmin ediniz: ").lower()

    #kullanıcıdan gelen harfin secilmiş kelime içinde olup olmadığını kontrol edelim
    #eğer içinde var ise görünecek kelimedeki "_" yerler bulunan harfle yer değiştirsin
    uzunluk=len(secilmis_kelime)
    for i in range(uzunluk):
        if tahmin==secilmis_kelime[i]:
            gorunen_kelime[i]=tahmin


    #tahnmin edilen harf seçilmiş kelime içinde yoksa can hakkını 1 düşür
    if tahmin not in secilmis_kelime:
        lives-=1
        if lives==0:
            print("\nOyun Sona Erdi, KAYBETTİNİZ!!")
            print(f"\nBulmaya çalıştığımız kelime {secilmis_kelime} idi.")
            oyun_sonu=False
    #buradada ekranda görünen çizili kelimede çizgi kalmadığında kullanıcının kazandığı anlamına gelir ve yine loop u durdurmalıyız.
    if "_" not in gorunen_kelime:
        print("\nOyun Sona Erdi, KAZANDINIZ!!!")
        oyun_sonu=False

    print(asamalar[lives])
    print(' '.join(gorunen_kelime))

    #Burada kullanıcı deneyimini arttırmak için her tahminde kaç tane bulduğunu veya bulamadığını belirtiyoruz
    #Ayrıca oyunun sonunda tahmin sayılarının söylemesin diye alttaki ilk if statement ının yazdık, yani hala oyun devam ediyorken sonuç yaz yoksa yazma. Oyun bittiğinde yazılacak çıktılar 45-54 satırlar arası
    adet=secilmis_kelime.count(tahmin)
    if "_" in gorunen_kelime and lives!=0:
        if tahmin in secilmis_kelime:
            print(f"\n{tahmin} harfini tahmin ettiniz ve {adet} adet buldunuz")
        else:
            print(f"\n{tahmin} harfini tahmin ettiniz ne yazıkki bulamadınız.")