import string

# 1. Adım: Alfabeyi tanımlıyoruz
alphabet = string.ascii_letters

# Verilen cümle
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

# 2. Adım: Harf sayımı için boş bir sözlük oluşturuyoruz
count_letters = {}

# 3. Adım: Cümledeki her bir karakteri döngüyle kontrol ediyoruz
for letter in sentence:
    # Sadece alfabede olan (büyük/küçük) harfleri sayıyoruz (boşlukları elemek için)
    if letter in alphabet:
        # Eğer harf sözlükte zaten varsa sayısını 1 artırıyoruz
        if letter in count_letters:
            count_letters[letter] += 1
        # Eğer harf sözlükte yoksa 1 değeriyle sözlüğe ekliyoruz
        else:
            count_letters[letter] = 1

# Sonucu görmek için sözlüğü yazdıralım
print(count_letters)