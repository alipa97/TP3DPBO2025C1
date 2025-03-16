from Cpu import Cpu
from Harddrive import Harddrive
from Ram import Ram

class Komputer:
    def __init__(self, nama="", cpu=None, ram_list=None, harddrive=None):
        self.nama = nama
        self.cpu = cpu if cpu else Cpu()
        self.ram_list = ram_list if ram_list else []
        self.harddrive = harddrive if harddrive else Harddrive()

    def set_nama(self, nama):
        self.nama = nama

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_ram(self, ram_list):
        self.ram_list = ram_list

    def set_harddrive(self, harddrive):
        self.harddrive = harddrive

    def add_ram(self, ram):
        self.ram_list.append(ram)

    def get_nama(self):
        return self.nama

    def get_cpu(self):
        return self.cpu

    def get_ram_list(self):
        return self.ram_list

    def get_harddrive(self):
        return self.harddrive
