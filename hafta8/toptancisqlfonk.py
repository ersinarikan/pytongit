import sqlite3
class sql:
    def __init__(self):
        self.conn = sqlite3.connect("Toptanci.db")
        self.cur = self.conn.cursor()

    def create(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS depo("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "bakliyat_ismi TEXT,"
                        "depo_numarasi INTEGER,"
                        "adet INTEGER,"
                        "kg INTEGER)")
        self.conn.commit()



    def ekle(self, bakliyat_ismi, depo_numarasi, adet, kg):
        self.cur.execute("INSERT INTO depo(bakliyat_ismi, depo_numarasi,adet,kg) VALUES(?,?,?,?)",
                         (bakliyat_ismi, depo_numarasi, adet, kg))
        self.conn.commit()

    def kontrol(self, bakliyat_ismi, depo_numarasi, kg):
        print(bakliyat_ismi, depo_numarasi, kg)
        sayi=-1
        try:
            self.cur.execute("SELECT SUM(adet) FROM depo where bakliyat_ismi  =? AND depo_numarasi = ? AND kg = ?",(bakliyat_ismi, depo_numarasi, kg))
            kutu1 = self.cur.fetchall()
            print("Kutu1 değeri",kutu1)
            sayi=kutu1[0][0]
        except:
            print("HATA")
        print("sayi",sayi)
        if sayi: return sayi
        else: return -1

    def rapor1(self):

        self.cur.execute("SELECT SUM(kg) FROM depo where bakliyat_ismi  =? ", ("Mercimek",))
        kilogram = self.cur.fetchall()
        print("-" * 50)
        print("Depolarda bulunan toplam Mercimek",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo where bakliyat_ismi  =? ", ("Nohut",))
        kilogram = self.cur.fetchall()
        print("Depolarda bulunan toplam Nohut",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo where bakliyat_ismi  =? ", ("Fasulye",))
        kilogram = self.cur.fetchall()
        print("Depolarda bulunan toplam Fasulye",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo where bakliyat_ismi  =? ", ("Pirinç",))
        kilogram = self.cur.fetchall()
        print("Depolarda bulunan toplam Pirinç",kilogram[0][0], "KG dır.")
        print("-"*50)
    def rapor2(self):
        self.cur.execute("SELECT SUM(kg) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Mercimek", 1,))
        kilogram = self.cur.fetchall()
        self.cur.execute("SELECT SUM(adet) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Mercimek", 1,))
        adet=self.cur.fetchall()
        print("-" * 50)
        print("1 Numaralı Depoda Mevcut ", adet[0][0], " Kutu Mercimek Toplam",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Nohut", 1,))
        kilogram = self.cur.fetchall()
        self.cur.execute("SELECT SUM(adet) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Nohut", 1,))
        adet=self.cur.fetchall()
        print("1 Numaralı Depoda Mevcut ", adet[0][0], " Kutu Nohut Toplam",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Pirinc", 1,))
        kilogram = self.cur.fetchall()
        self.cur.execute("SELECT SUM(adet) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Pirinc", 1,))
        adet=self.cur.fetchall()
        print("1 Numaralı Depoda Mevcut ", adet[0][0], " Kutu Pirinc Toplam",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Fasulye", 1,))
        kilogram = self.cur.fetchall()
        self.cur.execute("SELECT SUM(adet) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Fasulye", 1,))
        adet=self.cur.fetchall()
        print("1 Numaralı Depoda Mevcut ", adet[0][0], " Kutu Fasulye Toplam",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Mercimek", 2,))
        kilogram = self.cur.fetchall()
        self.cur.execute("SELECT SUM(adet) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Mercimek", 2,))
        adet=self.cur.fetchall()
        print("-" * 50)
        print("2 Numaralı Depoda Mevcut ", adet[0][0], " Kutu Mercimek Toplam",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Nohut", 2,))
        kilogram = self.cur.fetchall()
        self.cur.execute("SELECT SUM(adet) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Nohut", 2,))
        adet=self.cur.fetchall()
        print("2 Numaralı Depoda Mevcut ", adet[0][0], " Kutu Nohut Toplam",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Pirinc", 2,))
        kilogram = self.cur.fetchall()
        self.cur.execute("SELECT SUM(adet) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Pirinc", 2,))
        adet=self.cur.fetchall()
        print("2 Numaralı Depoda Mevcut ", adet[0][0], " Kutu Pirinc Toplam",kilogram[0][0], "KG dır.")
        self.cur.execute("SELECT SUM(kg) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Fasulye", 2,))
        kilogram = self.cur.fetchall()
        self.cur.execute("SELECT SUM(adet) FROM depo WHERE bakliyat_ismi = ? AND depo_numarasi = ?", ("Fasulye", 2,))
        adet=self.cur.fetchall()
        print("2 Numaralı Depoda Mevcut ", adet[0][0], " Kutu Fasulye Toplam",kilogram[0][0], "KG dır.")
        print("-" * 50)
