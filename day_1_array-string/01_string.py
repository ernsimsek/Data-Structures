harf = "a"
print(harf)

tek_tirnak = "a"
cift_tirnak = 'a'

coklu_satir = """birden fazla satirdan
oluşan bir string"""
print(coklu_satir)

index = "Bu bir string index denemesidir"
print(index[0])
print(index[-1])
print(index[3:6])

s = "bu ikinci string"

s1 = 'B' + s[1:]            #? s stringinin birinci karakterden sonrasını alıp 'B' ile birleştirdik.
print(s1)

# del s                     #? del ile değişkeni sildikten sonra s stringine ulaşamıyoruz. 
# print(s)

s2 = "ucuncu"

s3 = s1.replace("ikinci", s2)   #? değiştirmek istediğimiz string de replace metodunu kullanıyoruz. 
                                #? ilk parametreye değiştirmek istediğimiz yeri ikinciye ise değiştirilecek kısmın yeni değerini giriyoruz.
print(s3)

print(len(s3))              #? len string in uzunluğunu verir


print(s3.upper())             #? upper tüm karakterleri büyük yapar
print(s3.lower())             #? lower tüm karakterleri küçük yapar


bosluk = "               string               "
print(bosluk)
print(bosluk.strip())         #? strip stringin başında veya sonunda boşluk varsa onları kaldırır


m1 = "merhaba"
m2 = "dunya"
m3 = m1 + m2        #? string leri birleştirme işlemi
print(m3)
print(m3 * 5)       #? tekrarlamasını istiyorsak bir sayıyla çarparız

isim = "alice"
print(f"isim: {isim}") #? tırnaktan önce f string i yazarsak parantez içinde string değişkeni kullanabiliriz.

isim = "eren"

print("e" in isim)  #? in string için de sorgulama yapar
print("k" in isim)





