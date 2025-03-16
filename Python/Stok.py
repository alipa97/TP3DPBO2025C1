from Komputer import Komputer

class Stok:
    def __init__(self, jumlah=0, komputer=None):
        self.jumlah = jumlah
        self.komputer = komputer if komputer else Komputer()

    def set_jumlah(self, jumlah):
        self.jumlah = jumlah

    def set_komputer(self, komputer):
        self.komputer = komputer

    def get_jumlah(self):
        return self.jumlah

    def get_komputer(self):
        return self.komputer
