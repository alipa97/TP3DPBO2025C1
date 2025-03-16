#include <bits/stdc++.h>
#include "Cpu.cpp"
#include "Ram.cpp"
#include "Harddrive.cpp"
#include "Komputer.cpp"
#include "Stok.cpp"
#include "Penjualan.cpp"
#include "Toko.cpp"

using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);

    // Buat objek CPU, RAM, dan Harddrive
    Cpu cpu(8, 3.4, "Intel", "Core i7");
    Ram ram1(16, "DDR5", "Corsair", "Vengeance");
    Harddrive harddrive(1024, "SSD", "Samsung", "Evo");

    // Buat objek komputer
    Komputer komputer("PC ALIFA", cpu, {ram1, Ram(8, "DDR4", "Corsair", "Vengeance")}, harddrive);
    komputer.addRam(Ram(16, "DDR5", "Kingston", "FURY"));

    // Buat objek Toko dengan Stok dan Penjualan
    Toko toko("Toko Komputer Jaya", "Jl. Merdeka No. 123", 10, "2025-03-16", 15000000, komputer);

    // Tampilkan Informasi Komputer
    cout << "======================================" << endl;
    cout << "        INFORMASI KOMPUTER           " << endl;
    cout << "======================================" << endl;
    cout << "Nama      : " << komputer.getNama() << endl;
    cout << "CPU       : " << komputer.getCpu().getMerk() << " " << komputer.getCpu().getNama()
         << " (" << komputer.getCpu().getJumlahCore() << " Core) ~" 
         << komputer.getCpu().getKecepatanGHz() << "GHz" << endl;
    
    for (Ram& ram : komputer.getRamList()) {
        cout << "RAM       : " << ram.getMerk() << " " << ram.getNama()
             << " (" << ram.getKapasitasGB() << " GB) " << ram.getDdr() << endl;
    }

    cout << "Harddrive : " << komputer.getHarddrive().getTipeDrive() << " "
         << komputer.getHarddrive().getMerk() << " " << komputer.getHarddrive().getNama()
         << " (" << komputer.getHarddrive().getKapasitasGB() << " GB)" << endl;

    cout << "\n======================================" << endl;
    cout << "        INFORMASI TOKO               " << endl;
    cout << "======================================" << endl;
    cout << "Nama Toko  : " << toko.getNamaToko() << endl;
    cout << "Alamat     : " << toko.getAlamat() << endl;
    cout << "Stok       : " << toko.getJumlah() << " unit" << endl;

    cout << "\n======================================" << endl;
    cout << "        INFORMASI PENJUALAN           " << endl;
    cout << "======================================" << endl;
    cout << "Tanggal    : " << toko.getTanggal() << endl;
    cout << "Harga      : Rp " << toko.getHarga() << endl;

    return 0;
}
