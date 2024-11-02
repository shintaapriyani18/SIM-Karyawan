import mysql.connector

class Connection:
    def __init__(self):
        self.conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost", #localhost
        database="dbpegawai")

        self.cursor = self.conn.cursor()

        if self.conn.is_connected():
            print("Berhasil terhubung ke database")
            
    def addPegawai(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        print("Berhasil menambah data pegawai ke database")
        
    def updatePegawai(self, sql, nama, jabatan, gajipokok, jumlahanak, tunjangananak, tunjanganjabatan, ppn, jamkerja, tunjanganlembur, gajibulan, gajitahun, noinduk):
        self.cursor.execute(sql, (nama, jabatan, gajipokok, jumlahanak, tunjangananak, tunjanganjabatan, ppn, jamkerja, tunjanganlembur, gajibulan, gajitahun, noinduk))
        self.conn.commit()
        print("Berhasil mengubah data pegawai ke database")
        
    def deletePegawai(self, sql, noinduk):
        self.cursor.execute(sql, (noinduk,))
        self.conn.commit()
        print("Berhasil menghapus data pegawai dari database")
        
    def showPegawai(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
        
    def searchPegawai(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result
