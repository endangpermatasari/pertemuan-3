S = float(input("masukkan sisi: "))
P =input("pilih luas atau keliling: ")
Persegi = {"luas" : S*S, "keliling": 4*S}
print(Persegi.get(P, 'Oops, hanya bisa input "luas" atau "keliling". Periksa kembali input-an Anda'))