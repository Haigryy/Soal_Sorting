import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    kategori = maps[index]
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        # > untuk ascending (tersedikit ke terbanyak)
        if rev == False:
            while j >= 0 and data[j][kategori] > key[kategori]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        else:
            while j >= 0 and data[j][kategori] < key[kategori]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
           # Kerjakan disini
    
    # Jangan Dihapus
    show_data(data)

sort_by(data, "nama")
sort_by(data, "nim")
sort_by(data, "presensi")
sort_by(data, "presensi", True)


    
