from Komputer import Komputer

class Penjualan:
    def __init__(self, tanggal="", harga=0, komputer=None):
        self.tanggal = tanggal
        self.harga = harga
        self.komputer = komputer if komputer else Komputer()

    def set_tanggal(self, tanggal):
        self.tanggal = tanggal

    def set_harga(self, harga):
        self.harga = harga

    def set_komputer(self, komputer):
        self.komputer = komputer

    def get_tanggal(self):
        return self.tanggal

    def get_harga(self):
        return self.harga

    def get_komputer(self):
        return self.komputer
