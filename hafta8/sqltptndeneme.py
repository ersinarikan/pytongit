import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('depo.db')
cursor = conn.cursor()

# Tabloyu oluştur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS depo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        depo_no INTEGER,
        urun TEXT,
        miktar INTEGER
    )
''')
conn.commit()

# Mevcut ürünler ve depolar
urunler = {1: 'mercimek', 2: 'nohut', 3: 'pirinç', 4: 'fasulye'}
depolar = {1, 2}


def depo_giris():
    depo_no = int(input("Hangi depoya giriş yapmak istiyorsunuz? (1 veya 2): "))
    urun_secim = int(input("Hangi ürünü eklemek istiyorsunuz?\n1. Mercimek\n2. Nohut\n3. Pirinç\n4. Fasulye\nSeçim: "))
    if urun_secim not in urunler:
        print("Geçersiz ürün seçimi.")
        return

    urun = urunler[urun_secim]
    miktar = int(input("Miktarı girin (5, 10 veya 20): "))

    cursor.execute('''
        UPDATE depo
        SET miktar = miktar + ?
        WHERE depo_no = ? AND urun = ?
    ''', (miktar, depo_no, urun))

    if cursor.rowcount == 0:
        cursor.execute('''
            INSERT INTO depo (depo_no, urun, miktar)
            VALUES (?, ?, ?)
        ''', (depo_no, urun, miktar))
    conn.commit()
    print(f"{miktar} kg {urun} depoya başarıyla eklenmiştir.")


def depo_cikis():
    depo_no = int(input("Hangi depodan çıkış yapmak istiyorsunuz? (1 veya 2): "))
    urun_secim = int(input("Hangi ürünü çıkarmak istiyorsunuz?\n1. Mercimek\n2. Nohut\n3. Pirinç\n4. Fasulye\nSeçim: "))
    if urun_secim not in urunler:
        print("Geçersiz ürün seçimi.")
        return

    urun = urunler[urun_secim]
    miktar = int(input("Miktarı girin (5, 10 veya 20): "))

    cursor.execute('''
        UPDATE depo
        SET miktar = miktar - ?
        WHERE depo_no = ? AND urun = ? AND miktar >= ?
    ''', (miktar, depo_no, urun, miktar))

    if cursor.rowcount == 0:
        print(f"Uyarı: Depoda yeterli miktarda {urun} bulunmamaktadır.")
    else:
        conn.commit()
        print(f"{miktar} kg {urun} depodan başarıyla çıkarılmıştır.")


def depo_rapor():
    cursor.execute('''
        SELECT depo_no, urun, SUM(miktar) AS toplam_miktar
        FROM depo
        GROUP BY depo_no, urun
    ''')

    rows = cursor.fetchall()
    print("Depo Raporu:")
    for row in rows:
        print(f"Depo {row[0]}, {row[1]}: {row[2]} kg")


# Kullanıcı arayüzü
while True:
    print("\n1. Depo Girişi\n2. Depo Çıkışı\n3. Depo Raporu\n4. Çıkış")
    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")

    if secim == '1':
        depo_giris()
    elif secim == '2':
        depo_cikis()
    elif secim == '3':
        depo_rapor()
    elif secim == '4':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
