import cmd
print("=" * 60)
print("JibranTechDOS OS [Beta Version 0.1.4]")
print("Copyright © 2021 All Right Reserved")
print("=" * 60,"\n")

print("Ketik 'help' Untuk Melihat list command")
l = 1

while l < 7:
    perintah = input("JibranTechDOS@Windows-[~]-$ ")

    if "help" in perintah:
        print("\nList Command Di JibranTechDOS OS")
        print("math = Masuk ke Aplikasi Matematika")
        print("infosistem = informasi sistem JibranTechDOS OS")
        print("tentang = Tentang Aplikasi Matematika")

    elif "math" in perintah:
        print("\nketik 'list' untuk Melihat List Command Di Matematika")
        f = 1
        while f < 7:
            mathperintah = input("Matematika -$ ")
            if "list" in mathperintah:
                print("\nList Command Di Matematika")
                print("konsu = konversi suhu")
                print("tahkab = Menentukan tahun kabisat")
                print("kalk = Kalkulator")
                print("bilgangen = Menentukan Bilangan Ganjil Dan Genap")

            elif "kalk" in mathperintah:
                print("\nSelamat Datang di Kalkukator")
                print("Menu")
                print("1. Penjumlahan")
                print("2. Pengurangan")
                print("3. Perkalian")
                print("4. Pembagian")
                print("5. Keluar\n")

                q = 1
                while q < 7:
                    pilih = int(input("Pilih Nomor Menu: "))

                    if pilih == 1:
                        bilangan1 = int(input("Masukan Bilangan Pertama: "))
                        bilangan2 = int(input("Masukan Bilangan Kedua: "))

                        hasil = bilangan1 + bilangan2

                        print("Hasilnya Adalah:", hasil)

                    elif pilih == 2:
                        bilangan1 = int(input("Masukan Bilangan Pertama: "))
                        bilangan2 = int(input("Masukan Bilangan Kedua: "))

                        hasil = bilangan1 - bilangan2

                        print("Hasilnya Adalah:", hasil)

                    elif pilih == 3:
                        bilangan1 = int(input("Masukan Bilangan Pertama: "))
                        bilangan2 = int(input("Masukan Bilangan Kedua: "))

                        hasil = bilangan1 * bilangan2

                        print("Hasilnya Adalah:", hasil)

                    elif pilih == 4:
                        bilangan1 = int(input("Masukan Bilangan Pertama: "))
                        bilangan2 = int(input("Masukan Bilangan Kedua: "))

                        hasil = bilangan1 / bilangan2

                        print("Hasilnya Adalah:", hasil)

                    elif pilih == 5:
                        q + 7
                        break

                    else:
                        print("Menu Yang Anda Masukan Salah")

            elif "konsu" in mathperintah:
                def konversiSuhu(suhu):
                    drjt = int(suhu[:-1])
                    inputan = suhu[-1]

                    if inputan.upper() == "C":
                        hasil1 = float((9 * drjt) / 5 + 32)
                        hasil2 = float(drjt + 273.15)
                        hasil3 = float(4 / 5 * drjt)
                        jenisX = "Celcius"
                        jenis1 = "Fahrenheit"
                        jenis2 = "Kelvin"
                        jenis3 = "Reamur"
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil1), jenis1)
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil2), jenis2)
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil3), jenis3)

                    elif inputan.upper() == "F":
                        hasil1 = float((drjt - 32) * 5 / 9)
                        hasil2 = float(((drjt - 32) * 5 / 9) + 273.15)
                        hasil3 = float(4 / 9 * (drjt - 32))
                        jenisX = "Fahrenheit"
                        jenis1 = "Celsius"
                        jenis2 = "Kelvin"
                        jenis3 = "Reamur"
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil1), jenis1)
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil2), jenis2)
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil3), jenis3)

                    elif inputan.upper() == "K":
                        hasil1 = float(drjt - 273.15)
                        hasil2 = float(((drjt - 273.15) * 9 / 5) + 32)
                        hasil3 = float(4 / 5 * (drjt - 273))
                        jenisX = "Kelvin"
                        jenis1 = "Celcius"
                        jenis2 = "Fahrenheit"
                        jenis3 = "Reamur"
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil1), jenis1)
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil2), jenis2)
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil3), jenis3)

                    elif inputan.upper() == "R":
                        hasil1 = float((5 / 4) * drjt)
                        hasil2 = float((9 / 4 * drjt) + 32)
                        hasil3 = float((5 / 4 * drjt) + 273)
                        jenisX = "Reamur"
                        jenis1 = "Celcius"
                        jenis2 = "Fahrenheit"
                        jenis3 = "Kelvin"
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil1), jenis1)
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil2), jenis2)
                        print(drjt, jenisX, "=", "{:.1f}".format(hasil3), jenis3)

                    else:
                        print("Inputan tidak sesuai!! Perhatikan Penulisan Input")


                i = 0
                print("Program Konversi Suhu")
                while i == 0:
                     temp = input("\nMasukan suhu? (Misal: 30C, 20F, 21K, 44R): ")
                     konversiSuhu(temp)

                     lagi = int(input("Hitung lagi?1=ya & 0=tidak = "))
                     if (lagi == 1):
                        i = 0
                     elif (lagi != 1):
                        i = 1
            elif "exit" in mathperintah:
                iyaatautidak = input("Apa kamu yakin (y/t): ")
                if "y" in iyaatautidak:
                    print("Keluar Aplikasi Dengan Kode MTx3643e3x1T")
                    f + 7
                    break
                elif "t" in iyaatautidak:
                    print("membatalkan keluar")
                else:
                    print("Anda Salah Memasukan Pilihan, Coba Lagi")
            elif "tahkab" in mathperintah:
                tahun = int(input("Masukan Tahun: "))
                if ((tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)):
                    print(tahun,"Merupakan Tahun Kabisat")
                else:
                    print(tahun,"Bukan Merupakan Tahun Kabisat")
            elif "bilgangen" in mathperintah:
                bil = int(input("Masukan Bilangan :"))

                if bil % 2 == 0:
                    print(" %d Merupakan Bilangan Genap" % bil)
                else:
                    print("%d Merupakan Bilangan Ganjil" % bil)
            else:
                print("'",mathperintah,"' Tidak ada atau salah ejaan")


    elif "assoc" in perintah:
        print(".001=WinRAR")
        print(".386=vxdfile")
        print(".3g2=WMP11.AssocFile.3G2")
        print(".3gp=WMP11.AssocFile.3GP")
        print(".3gp2=WMP11.AssocFile.3G2")
        print(".3gpp=WMP11.AssocFile.3GP")
        print(".7z=WinRAR")
        print(".AAC=WMP11.AssocFile.ADTS")
        print(".accda=Access.ACCDAExtension.16")
        print(".accdb=Access.Application.16")
        print(".accdc=Access.ACCDCFile.16")
        print(".accde=Access.ACCDEFile.16")
        print(".ade=Access.ADEFile.16")
        print(".adn=Access.BlankProjectTemplate.16")
        print(".adp=Access.Project.16")
        print(".ADT=WMP11.AssocFile.ADTS")
        print(".ADTS=WMP11.AssocFile.ADTS")
        print(".aif=WMP11.AssocFile.AIFF")
        print(".aifc=WMP11.AssocFile.AIFF")
        print(".aiff=WMP11.AssocFile.AIFF")
        print(".ani=anifile")
        print(".appcontent-ms=ApplicationContent")

    elif "infosistem" in perintah:
        print("Informasi Sistem JibranTechDOS OS")
        print("Versi Aplikasi: bv0.1.4")
        print("Dibuat Oleh: JibranTech Security")
        print("Operasi Sistem: Microsoft Windows")
        print("Hak Cipta Dilindungi oleh Undang-Undang")
    elif "tentang" in perintah:
        print("Tentang JibranTech DOS OS\n")
        print("Aplikasi ini dibuat oleh Jibrantech Security, aplikasi ini kompatibel dengan OS Windows Dan Linux, ")
        print("aplikasi ini diprogramkan oleh Tim JibranTech Security menggunakan Python. PERINGATAN: 'Jangan Melakukan")
        print("bajak, mengambil karya Tim JibranTech Security,'")
        print("Aplikasi ini dirilis tahun 07 Desember 2021 dengan resmi. Untuk mau rekomendasi, silahkan hubungi JibranTech ")
        print("Security di email: jibrantech@gmail.com\n")
        print("Undang-Undang NO 19 Tahun 2002 Pasal 72 Ayat 1 dan Ayat 2 Tentang Hak Cipta")
        print("1. Barangsiapa dengan sengaja dan tanpa hak melakukan perbuatan")
        print("sebagaimana dimaksud dalam Pasal 2 ayat (1) atau Pasal 49 ayat")
        print("(1) dan ayat (2) dipidana dengan pidana penjara masing-masing")
        print("paling singkat 1 (satu) bulan dan/atau denda paling sedikit Rp")
        print("1.000.000,00 (satu juta rupiah), atau pidana penjara paling")
        print("lama 7 (tujuh) tahun dan/atau denda paling banyak Rp")
        print("5.000.000.000,00 (lima miliar rupiah).\n")
        print("2.  Barangsiapa dengan sengaja menyiarkan, memamerkan,")
        print("mengedarkan, atau menjual kepada umum suatu Ciptaan atau")
        print("barang hasil pelanggaran Hak Cipta atau Hak Terkait")
        print("sebagaimana dimaksud pada ayat (1) dipidana dengan pidana")
        print("penjara paling lama 5 (lima) tahun dan/atau denda paling")
        print("banyak Rp 500.000.000,00 (lima ratus juta rupiah).")


    elif "exit" in perintah:

        iyaatautidak = input("Apa kamu yakin? (y/t): ")
        if "y" in iyaatautidak:
            print("Keluar Program dengan Kode Keluar 30879")
            l + 7
            break
        elif "t" in iyaatautidak:
            print("Membatalkan Keluar")

        else:
            print("Anda Salah Memasukan Pilihan, Coba Lagi")
    else:
        print("'",perintah,"' Tidak ada atau salah ejaan")
