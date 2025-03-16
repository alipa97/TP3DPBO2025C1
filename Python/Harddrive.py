from Komponen import Komponen

class Harddrive(Komponen):
    def __init__(self, kapasitas_gb=0, tipe_drive="", merk="", nama=""):
        super().__init__(merk, nama)
        self.kapasitas_gb = kapasitas_gb
        self.tipe_drive = tipe_drive

    def set_kapasitas_gb(self, kapasitas_gb):
        self.kapasitas_gb = kapasitas_gb

    def set_tipe_drive(self, tipe_drive):
        self.tipe_drive = tipe_drive

    def get_kapasitas_gb(self):
        return self.kapasitas_gb

    def get_tipe_drive(self):
        return self.tipe_drive
