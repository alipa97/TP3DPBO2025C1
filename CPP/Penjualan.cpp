#pragma once
#include <iostream>
#include <string>
#include "Komputer.cpp"

using namespace std;

class Penjualan {
private:
    string tanggal;
    int harga;
    Komputer komputer;
public:
    Penjualan()
    {


    }


    Penjualan(string tanggal, int harga, Komputer komputer)
    {
        this->tanggal = tanggal;
        this->harga = harga;
        this->komputer = komputer;
    }


    void settanggal(string tanggal)
    {
        this->tanggal = tanggal;
    }

    void setHarga(int harga)
    {
        this->harga = harga;
    }

    void setKomputer(Komputer Komponen)
    {
        this->komputer = komputer;
    }

    string getTanggal()
    {
        return tanggal;
    }

    int getHarga()
    {
        return harga;
    }

    Komputer getKomputer()
    {
        return this->komputer;
    }

    ~Penjualan()
    {




    }
};
