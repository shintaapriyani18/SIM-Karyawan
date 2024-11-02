from connection import Connection
from pegawai import Pegawai

connect =  Connection()

def ShowMenu():
    print("=========================================================")
    print("                    Selamat Datang                       ")
    print("=========================================================")
    print("Pilih Menu: ")
    print("1. Tambah Data Pegawai")
    print("2. Edit Data Pegawai")
    print("3. Hapus Data Pegawai")
    print("4. Cetak Data Pegawai")
    print("5. Exit")
    print("=========================================================")
    inputmenu = int(input("Masukan Nomor Menu Yang Kamu Pilih: "))
    print("=========================================================")
    
    if inputmenu == 1:
        TambahDataPegawai()
        ShowMenu()
    elif inputmenu == 2:
        EditDataPegawai()
        ShowMenu()
    elif inputmenu == 3:
        HapusDataPegawai()
        ShowMenu()
    elif inputmenu == 4:
        CetakDataPegawai()
        ShowMenu()
    elif inputmenu == 5:
        Exit()
        ShowMenu()
    else:
        print("Nomor Menu yang Anda Masukan Tidak Valid")
    
    
def TambahDataPegawai():
    nama = str(input("Masukan Nama: "))
    noinduk = int(input("Masukan No Induk: "))
    
    print("Pilihan Jabatan: ")
    print("1. Data Scientist")
    print("2. Programmer")
    print("3. Data Analyst")
    print("4. Database Engineer")
    
    jabatan = int(input("Masukan Pilihan Jabatan (contoh:3) : "))
    
    if jabatan == 1:
        jabatan = "Data Scientist"
        gajipokok = 8000000
        print("Jabatan: ", jabatan)
        print("Gaji Pokok: ", gajipokok)
         
        jumlahanak = int(input("Masukan Jumlah Anak: "))
        
        tunjangannak = (jumlahanak * 0.03) * gajipokok
        print("Tunjangan Anak: ", tunjangannak)
    
        tunjanganjabatan = gajipokok * 0.05
        print("Tunjangan Jabatan: ", tunjanganjabatan)
    
        ppn = 0.01 * gajipokok
        print("PPN: ", ppn)
        
        jamkerja = int(input("Masukan Jam Kerja / Bulan (minimal 192): "))
        
        if jamkerja > 192:
            totaljam = jamkerja - 192
            tunjanganlembur = totaljam * 25000
            print("Tunjangan Lembur: ", tunjanganlembur)
        else:
            tunjanganlembur = 0
            print("Tunjangan Lembur: ", tunjanganlembur)
        
        gajibulan = (gajipokok + tunjangannak + tunjanganjabatan + tunjanganlembur) - ppn
        print("Gaji / Bulan: ", gajibulan)
        gajitahun = gajibulan * 12
        print("Gaji / Tahun: ", gajitahun)
            
    elif jabatan == 2:
        jabatan = "Programmer"
        gajipokok = 7500000
        print("Jabatan: ", jabatan)
        print("Gaji Pokok: ", gajipokok)
          
        jumlahanak = int(input("Masukan Jumlah Anak: "))
        
        tunjangannak = (jumlahanak * 0.03) * gajipokok
        print("Tunjangan Anak: ", tunjangannak)
    
        tunjanganjabatan = gajipokok * 0.05
        print("Tunjangan Jabatan: ", tunjanganjabatan)
    
        ppn = 0.01 * gajipokok
        print("PPN: ", ppn)
        
        jamkerja = int(input("Masukan Jam Kerja / Bulan (minimal 192): "))
        
        if jamkerja > 192:
            totaljam = jamkerja - 192
            tunjanganlembur = totaljam * 25000
            print("Tunjangan Lembur: ", tunjanganlembur)
        else:
            tunjanganlembur = 0
            print("Tunjangan Lembur: ", tunjanganlembur)
        
        gajibulan = (gajipokok + tunjangannak + tunjanganjabatan + tunjanganlembur) - ppn
        print("Gaji / Bulan: ", gajibulan)
        gajitahun = gajibulan * 12
        print("Gaji / Tahun: ", gajitahun)
        
    elif jabatan == 3:
        jabatan = "Data Analyst"
        gajipokok = 5000000
        print("Jabatan: ", jabatan)
        print("Gaji Pokok: ", gajipokok)
        
        jumlahanak = int(input("Masukan Jumlah Anak: "))
        
        tunjangannak = (jumlahanak * 0.03) * gajipokok
        print("Tunjangan Anak: ", tunjangannak)
    
        tunjanganjabatan = gajipokok * 0.05
        print("Tunjangan Jabatan: ", tunjanganjabatan)
    
        ppn = 0.01 * gajipokok
        print("PPN: ", ppn)
        
        jamkerja = int(input("Masukan Jam Kerja / Bulan (minimal 192): "))
        
        if jamkerja > 192:
            totaljam = jamkerja - 192
            tunjanganlembur = totaljam * 25000
            print("Tunjangan Lembur: ", tunjanganlembur)
        else:
            tunjanganlembur = 0
            print("Tunjangan Lembur: ", tunjanganlembur)
        
        gajibulan = (gajipokok + tunjangannak + tunjanganjabatan + tunjanganlembur) - ppn
        print("Gaji / Bulan: ", gajibulan)
        gajitahun = gajibulan * 12
        print("Gaji / Tahun: ", gajitahun)
        
    elif jabatan == 4:
        jabatan = "Database Engineer"
        gajipokok = 5500000
        print("Jabatan: ", jabatan)
        print("Gaji Pokok: ", gajipokok)
           
        jumlahanak = int(input("Masukan Jumlah Anak: "))
        
        tunjangannak = (jumlahanak * 0.03) * gajipokok
        print("Tunjangan Anak: ", tunjangannak)
    
        tunjanganjabatan = gajipokok * 0.05
        print("Tunjangan Jabatan: ", tunjanganjabatan)
    
        ppn = 0.01 * gajipokok
        print("PPN: ", ppn)
        
        jamkerja = int(input("Masukan Jam Kerja / Bulan (minimal 192): "))
        
        if jamkerja > 192:
            totaljam = jamkerja - 192
            tunjanganlembur = totaljam * 25000
            print("Tunjangan Lembur: ", tunjanganlembur)
        else:
            tunjanganlembur = 0
            print("Tunjangan Lembur: ", tunjanganlembur)
        
        gajibulan = (gajipokok + tunjangannak + tunjanganjabatan + tunjanganlembur) - ppn
        print("Gaji / Bulan: ", gajibulan)
        gajitahun = gajibulan * 12
        print("Gaji / Tahun: ", gajitahun)
        
    data = "INSERT INTO pegawai VALUES ('" + str(noinduk) +"','" + nama + "','" + jabatan + "','" + str(gajipokok) + "','" + str(jumlahanak)  + "','" + str(tunjangannak) + "','" + str(tunjanganjabatan) + "','" + str(ppn) + "','" + str(jamkerja) + "','" + str(tunjanganlembur) + "','" + str(gajibulan) +"','" + str(gajitahun) + "') "
    connect.addPegawai(data)
   

def EditDataPegawai():
    noinduk = int(input("Masukan No Induk: "))
    
    searchdata = ("SELECT * FROM pegawai WHERE noinduk = %s")%(noinduk)
    hasil = connect.searchPegawai(searchdata)
    
    print("Nama Lama: ", hasil[1])
    nama = str(input("Masukan Nama Baru: "))
    
    print("Jabatan Lama: ", hasil[2])
    
    print("Pilihan Jabatan: ")
    print("1. Data Scientist")
    print("2. Programmer")
    print("3. Data Analyst")
    print("4. Database Engineer")
    
    jabatan = int(input("Masukan Pilihan Jabatan (contoh:3) : "))
    
    if jabatan == 1:
        jabatan = "Data Scientist"
        gajipokok = 8000000
        print("Jabatan: ", jabatan)
        print("Gaji Pokok: ", gajipokok)
        
        print("Jumlah Anak Lama: ", hasil[4]) 
        jumlahanak = int(input("Masukan Jumlah Anak Baru : "))
        
        tunjangannak = (jumlahanak * 0.03) * gajipokok
        print("Tunjangan Anak: ", tunjangannak)
    
        tunjanganjabatan = gajipokok * 0.05
        print("Tunjangan Jabatan: ", tunjanganjabatan)
    
        ppn = 0.01 * gajipokok
        print("PPN: ", ppn)
        
        print("Jam Kerja Lama: ", hasil[8])
        jamkerja = int(input("Masukan Jam Kerja / Bulan (minimal 192): "))
        
        if jamkerja > 192:
            totaljam = jamkerja - 192
            tunjanganlembur = totaljam * 25000
            print("Tunjangan Lembur: ", tunjanganlembur)
        else:
            tunjanganlembur = 0
            print("Tunjangan Lembur: ", tunjanganlembur)
        
        gajibulan = (gajipokok + tunjangannak + tunjanganjabatan + tunjanganlembur) - ppn
        print("Gaji / Bulan: ", gajibulan)
        gajitahun = gajibulan * 12
        print("Gaji / Tahun: ", gajitahun)
            
    elif jabatan == 2:
        jabatan = "Programmer"
        gajipokok = 7500000
        print("Jabatan: ", jabatan)
        print("Gaji Pokok: ", gajipokok)
        
        print("Jumlah Anak Lama: ", hasil[4]) 
        jumlahanak = int(input("Masukan Jumlah Anak Baru : "))
        
        tunjangannak = (jumlahanak * 0.03) * gajipokok
        print("Tunjangan Anak: ", tunjangannak)
    
        tunjanganjabatan = gajipokok * 0.05
        print("Tunjangan Jabatan: ", tunjanganjabatan)
    
        ppn = 0.01 * gajipokok
        print("PPN: ", ppn)
        
        print("Jam Kerja Lama: ", hasil[8])
        jamkerja = int(input("Masukan Jam Kerja / Bulan (minimal 192): "))
        
        if jamkerja > 192:
            totaljam = jamkerja - 192
            tunjanganlembur = totaljam * 25000
            print("Tunjangan Lembur: ", tunjanganlembur)
        else:
            tunjanganlembur = 0
            print("Tunjangan Lembur: ", tunjanganlembur)
        
        gajibulan = (gajipokok + tunjangannak + tunjanganjabatan + tunjanganlembur) - ppn
        print("Gaji / Bulan: ", gajibulan)
        gajitahun = gajibulan * 12
        print("Gaji / Tahun: ", gajitahun)
        
    elif jabatan == 3:
        jabatan = "Data Analyst"
        gajipokok = 5000000
        print("Jabatan: ", jabatan)
        print("Gaji Pokok: ", gajipokok)
        
        print("Jumlah Anak Lama: ", hasil[4]) 
        jumlahanak = int(input("Masukan Jumlah Anak Baru : "))
        
        tunjangannak = (jumlahanak * 0.03) * gajipokok
        print("Tunjangan Anak: ", tunjangannak)
    
        tunjanganjabatan = gajipokok * 0.05
        print("Tunjangan Jabatan: ", tunjanganjabatan)
    
        ppn = 0.01 * gajipokok
        print("PPN: ", ppn)
        
        print("Jam Kerja Lama: ", hasil[8])
        jamkerja = int(input("Masukan Jam Kerja / Bulan (minimal 192): "))
        
        if jamkerja > 192:
            totaljam = jamkerja - 192
            tunjanganlembur = totaljam * 25000
            print("Tunjangan Lembur: ", tunjanganlembur)
        else:
            tunjanganlembur = 0
            print("Tunjangan Lembur: ", tunjanganlembur)
        
        gajibulan = (gajipokok + tunjangannak + tunjanganjabatan + tunjanganlembur) - ppn
        print("Gaji / Bulan: ", gajibulan)
        gajitahun = gajibulan * 12
        print("Gaji / Tahun: ", gajitahun)
        
    elif jabatan == 4:
        jabatan = "Database Engineer"
        gajipokok = 5500000
        print("Jabatan: ", jabatan)
        print("Gaji Pokok: ", gajipokok)
           
        print("Jumlah Anak Lama: ", hasil[4]) 
        jumlahanak = int(input("Masukan Jumlah Anak Baru : "))
        
        tunjangannak = (jumlahanak * 0.03) * gajipokok
        print("Tunjangan Anak: ", tunjangannak)
    
        tunjanganjabatan = gajipokok * 0.05
        print("Tunjangan Jabatan: ", tunjanganjabatan)
    
        ppn = 0.01 * gajipokok
        print("PPN: ", ppn)
        
        print("Jam Kerja Lama: ", hasil[8])
        jamkerja = int(input("Masukan Jam Kerja / Bulan (minimal 192): "))
        
        if jamkerja > 192:
            totaljam = jamkerja - 192
            tunjanganlembur = totaljam * 25000
            print("Tunjangan Lembur: ", tunjanganlembur)
        else:
            tunjanganlembur = 0
            print("Tunjangan Lembur: ", tunjanganlembur)
        
        gajibulan = (gajipokok + tunjangannak + tunjanganjabatan + tunjanganlembur) - ppn
        print("Gaji / Bulan: ", gajibulan)
        gajitahun = gajibulan * 12
        print("Gaji / Tahun: ", gajitahun)
    
    editdata = "UPDATE pegawai SET namapegawai=%s, jabatan=%s, gajipokok=%s, jumlahanak=%s, tunjangananak=%s, tunjanganjabatan=%s, ppn=%s, jamkerja=%s, tunjanganlembur=%s, gajibulan=%s, gajitahun=%s WHERE noinduk=%s"
    connect.updatePegawai(editdata, nama, jabatan, gajipokok, jumlahanak, tunjangannak, tunjanganjabatan, ppn, jamkerja, tunjanganlembur, gajibulan, gajitahun, noinduk)

def HapusDataPegawai():
    noinduk = int(input("Masukkan Noinduk Pegawai: "))
    hapusdata = "DELETE FROM pegawai WHERE noinduk = %s"
    connect.deletePegawai(hapusdata, noinduk)

def CetakDataPegawai():
    selectAllPegawai = "SELECT * FROM pegawai"
    result = connect.showPegawai(selectAllPegawai)
    listProduk = []

    for row in result:
        listProduk.append(Pegawai(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
 
    for data in listProduk:
        print("NoInduk : " + str(data.noinduk) + "\nNAMA : " + data.nama + "\nJabatan " + data.jabatan + "\nGaji Pokok: " + str(data.gajipokok) + "\nJumlah Anak: " + str(data.jumlahanak) + "\nTunjangan Anak: " + str(data.tunjangananak) + "\nTunjangan Jabatan: " + str(data.tunjanaganjabatan) + "\nPPN: " + str(data.ppn) + "\nJam Kerja: " + str(data.jamkerja) + "\nTunjangan Lembur: " + str(data.tunjanganlembur) + "\nGaji Bulan: " + str(data.gajibulan) + "\nGaji Tahun: " + str(data.gajitahun))

def Exit():
    quit()

ShowMenu()      
