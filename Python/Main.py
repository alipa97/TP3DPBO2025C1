from Cpu import Cpu
from Ram import Ram
from Harddrive import Harddrive
from Komputer import Komputer
from Stok import Stok
from Penjualan import Penjualan
from Toko import Toko

# Buat objek CPU, RAM, dan Harddrive
cpu = Cpu(8, 3.4, "Intel", "Core i7")
ram1 = Ram(16, "DDR5", "Corsair", "Vengeance")
harddrive = Harddrive(1024, "SSD", "Samsung", "Evo")

# Buat objek komputer
komputer = Komputer("PC ALIFA", cpu, [ram1, Ram(8, "DDR4", "Corsair", "Vengeance")], harddrive)
komputer.add_ram(Ram(16, "DDR5", "Kingston", "FURY"))

# Buat objek Toko dengan Stok dan Penjualan
toko = Toko("Toko Komputer Jaya", "Jl. Merdeka No. 123", 10, "2025-03-16", 15000000, komputer)

# Tampilkan Informasi Komputer
print("=" * 38)
print("        INFORMASI KOMPUTER           ")
print("=" * 38)
print(f"Nama      : {komputer.get_nama()}")
print(f"CPU       : {komputer.get_cpu().get_merk()} {komputer.get_cpu().get_nama()} "
      f"({komputer.get_cpu().get_jumlah_core()} Core) ~{komputer.get_cpu().get_kecepatan_ghz()}GHz")

for ram in komputer.get_ram_list():
    print(f"RAM       : {ram.get_merk()} {ram.get_nama()} "
          f"({ram.get_kapasitas_gb()} GB) {ram.get_ddr()}")

print(f"Harddrive : {komputer.get_harddrive().get_tipe_drive()} "
      f"{komputer.get_harddrive().get_merk()} {komputer.get_harddrive().get_nama()} "
      f"({komputer.get_harddrive().get_kapasitas_gb()} GB)")

print("\n" + "=" * 38)
print("        INFORMASI TOKO               ")
print("=" * 38)
print(f"Nama Toko  : {toko.get_nama_toko()}")
print(f"Alamat     : {toko.get_alamat()}")
print(f"Stok       : {toko.get_jumlah()} unit")

print("\n" + "=" * 38)
print("        INFORMASI PENJUALAN           ")
print("=" * 38)
print(f"Tanggal    : {toko.get_tanggal()}")
print(f"Harga      : Rp {toko.get_harga()}")
