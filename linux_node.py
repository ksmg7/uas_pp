import math

pilihan = int(input())
if pilihan == 1:
	sisi = int(input())
	keliling = 4*sisi
	luas = sisi**2
if pilihan == 2:
	panjang = int(input())
	lebar = int(input())
	keliling = (2*panjang) + (2*lebar)
	luas = panjang * lebar
if pilihan == 3:
	alas = int(input())
	tinggi = int(input())
	keliling = math.sqrt(pow(alas,2) + pow(tinggi,2))
	luas = alas * tinggi / 2
if pilihan == 4:
	jari_jari = int(input())
	luas = 3.14 * jari_jari * jari_jari
	keliling = 2 * 3.14 * jari_jari

print("\n---------- Program menghitung bangun datar ----------")
print("----------       Pemrosesan Paralel        ----------")
print("----------             Hasil               ----------\n")

print("Keliling: ", keliling)
print("Luas: ", luas)
