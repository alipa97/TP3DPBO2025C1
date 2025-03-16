#pragma once
#include <iostream>
#include <string>
#include <vector>
#include "Stok.cpp"
#include "Penjualan.cpp"

using namespace std;

class Toko : public Stok, public Penjualan
{
private:
    string namaToko;
    string alamat;
public:
    Toko()
    {


    }


    Toko(string namaToko, string alamat, int jumlah, string tanggal, int harga, Komputer komputer) : Stok(jumlah, komputer), Penjualan(tanggal, harga, komputer)
    {
        this->namaToko = namaToko;
        this->alamat = alamat;
    }


    void setNamaToko(string namaToko)
    {
        this->namaToko = namaToko;
    }

    void setAlamat(string alamat)
    {
        this->alamat = alamat;
    }

    string getNamaToko()
    {
        return this->namaToko;
    }


    string getAlamat()
    {
        return this->alamat;
    }

    ~Toko()
    {


    }
};
