from Komponen import Komponen

class Ram(Komponen):
    def __init__(self, kapasitas_gb=0, ddr="", merk="", nama=""):
        super().__init__(merk, nama)
        self.kapasitas_gb = kapasitas_gb
        self.ddr = ddr

    def set_kapasitas_gb(self, kapasitas_gb):
        self.kapasitas_gb = kapasitas_gb

    def set_ddr(self, ddr):
        self.ddr = ddr

    def get_kapasitas_gb(self):
        return self.kapasitas_gb

    def get_ddr(self):
        return self.ddr
