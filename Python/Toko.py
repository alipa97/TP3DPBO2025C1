from Stok import Stok
from Penjualan import Penjualan

class Toko(Stok, Penjualan):
    def __init__(self, nama_toko="", alamat="", jumlah=0, tanggal="", harga=0, komputer=None):
        Stok.__init__(self, jumlah, komputer)
        Penjualan.__init__(self, tanggal, harga, komputer)
        self.nama_toko = nama_toko
        self.alamat = alamat

    def set_nama_toko(self, nama_toko):
        self.nama_toko = nama_toko

    def set_alamat(self, alamat):
        self.alamat = alamat

    def get_nama_toko(self):
        return self.nama_toko

    def get_alamat(self):
        return self.alamat
