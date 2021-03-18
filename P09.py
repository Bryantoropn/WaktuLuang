waktu1 = int(input("Masukkan banyaknya waktu luang orang ke 1: "))
waktu1_awal = [0 for i in range(waktu1)]
waktu1_akhir = [0 for i in range(waktu1)]

for i in range(waktu1):
    waktu1_awal[i] = str(input("Masukkan awal waktu orang 1 ke-" + str(i + 1) + ": "))
    waktu1_akhir[i] = str(input("Masukkan akhir waktu orang 1 ke-" + str(i + 1) + ": "))

waktu2 = int(input("Masukkan banyaknya waktu luang orang ke 2: "))
waktu2_awal = [0 for i in range(waktu2)]
waktu2_akhir = [0 for i in range(waktu2)]

for i in range(waktu2):
    waktu2_awal[i] = str(input("Masukkan awal waktu luang orang 2 ke-" + str(i + 1) + ": "))
    waktu2_akhir[i] = str(input("Masukkan akhir waktu luang orang 2 ke-" + str(i + 1) + ": "))

totalWaktu = waktu1 * waktu2
sama_awal = [0 for i in range(totalWaktu)]
sama_akhir = [0 for i in range(totalWaktu)]

m = 0
for i in waktu1_awal:
    for j in waktu2_awal:
        if (i >= j):
            sama_awal[m] = i
            m += 1
        else:
            sama_awal[m] = j
            m += 1

m = 0
for i in waktu1_akhir:
    for j in waktu2_akhir:
        if (i <= j):
            sama_akhir[m] = i
            m += 1
        else:
            sama_akhir[m] = j
            m += 1
            
count = 1
for i in range(totalWaktu):
    if (sama_awal[i] < sama_akhir[i]):
        print("Waktu luang kedua pihak ke-" + str(count) + ": " + sama_awal[i] + " - " + sama_akhir[i])
        count += 1