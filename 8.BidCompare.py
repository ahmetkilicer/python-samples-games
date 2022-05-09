#logonun yazılması
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

#Tüm tekliflerin yazılacağı boş bir dictionary nin oluşturulması
all_bids={}

#teklif verecek insan olduğu sürece while loop unun dönmesi
yes=True
while yes:

    #kullanıcılardan tekliflerin alınması
    names=input("What's Your name?: ")
    bids=int(input("What's your bid?: "))

    #Tekliflerin boş listeye eklemesi
    all_bids[names]=bids
    #daha fazla teklivarsa ekranı temizleyerek programın loopun başına döndürüyoruz
    more_bid=input("will more bids?(yes or no):").lower()
    if more_bid == "yes":
        #terminal temizleme komutu, bu sayede diğer teklif verenler göremeyecek
        import os
        os.system('cls'or'clr')
        continue

    #son tekliften sonra tekliflerin karşılaştırılması
    else:
        final_bid=0
        for i in all_bids:
            if all_bids[i]>final_bid:
                final_bid=all_bids[i]
                result=i
    os.system('cls')
    #Sonucun ekrana yazdırılması
    print(f"The Winner is {result} with {final_bid}")
    #döngünün durdurulması
    yes=False