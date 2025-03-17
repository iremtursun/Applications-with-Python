import random

kelimeler=["elma","armut","kiraz","muz","ayva","çilek","portakal","vişne","armut","erik","mandalina","nar"]
gerekli_harfler="abcçdefghıijklmnoöprsştyuüzw"
olusturulan_kelime=""
hak=5
ADAM_ASMACA_GORSLLERI = [
    """
      --------
      |    |
      |
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |    |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   /
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   / \
      |
    """
]

secili_kelime=random.choice(kelimeler)
print("Oyun Başlasın!")
print("Kelime: ", len(secili_kelime)*"_",secili_kelime)


while hak>0 :
    gercek_kelime=""
    for i in secili_kelime:
        if i in olusturulan_kelime:
            i+=gercek_kelime
        else:
            gercek_kelime+="_"
    
    if gercek_kelime == secili_kelime:
        print(gercek_kelime)
        print("Tebrikler kazandınız!")
        break
    print(ADAM_ASMACA_GORSLLERI[5 - hak])
    print("Hayvan adını tahmin edin:", gercek_kelime)
    print(f"Kalan hakkınız: {hak}")

    tahmin = input("Bir harf tahmin edin: ").lower()

    if tahmin in gerekli_harfler:
        olusturulan_kelime += tahmin
        if tahmin not in secili_kelime:
            hak -= 1
    else:
        print("Lütfen geçerli bir harf giriniz...")

else:
    print("Maalesef kaybettiniz. Doğru kelime:", secili_kelime)
