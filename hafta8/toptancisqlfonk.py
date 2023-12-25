import sqlite3
class sql:
    def __init__(self):
        self.conn=sqlite3.connect("Toptanci.db")
        self.cur=self.conn.cursor()
    def create(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS depo("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "bakliyat_ismi TEXT,"
                        "depo_numarasi INTEGER,"
                        "adet INTEGER,"
                        "kg INTEGER)")
        self.conn.commit()
    def ekle(self,bakliyat_ismi,depo_numarasi,adet,kg):
        self.cur.execute("INSERT INTO depo(bakliyat_ismi, depo_numarasi,adet,kg) VALUES(?,?,?,?)",
                         (bakliyat_ismi, depo_numarasi, adet, kg))
        self.conn.commit()
    def rapor1(self):
        # print(self.cur.execute("SELECT SUM(kg) FROM depo"))
        # self.conn.commit()
        self.cur.execute("SELECT * FROM depo")
        veriler=self.cur.fetchall()
        for veri in veriler:
            print("Bakliyat İsmi : ", veri[1])
            print("Depo Numarası : ", veri[2])
            print("Adet : ", veri[3])
            print("KG : ", veri[4])
            print("Toplam : ", veri[3]+veri[4])

