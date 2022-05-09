#|--------------------------------------------------HERHANGİ BİR AYIN KAÇ GÜN OLDUĞUNU HESAPLAMA--------------------------------------


#bir yılın şubat ayı 29 gün ise bu yılı leap year(Artık yıl denir) Artık yıllar, 4 ile kalansız bölünebilen yıllardır (400 ile bölünemeyen yüzyıl başları hariç).
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

#Her ayın normal gün sayısı listeden çekilir
def days_in_month(year,month):
  if month>12 or month<1:
    return "Invalid Month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  #Artık yıl ise ve ay şubat seçildiyse 29 döndürür
  if is_leap(year) and month==2:
    return 29
  else:
    return month_days[month-1]
  
#kullanıcıdan istediği yıl ve ayı alıyoruz
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












