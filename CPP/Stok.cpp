#pragma once
#include <iostream>
#include <string>
#include "Komputer.cpp"

using namespace std;

class Stok {
private:
    int jumlah;
    Komputer komputer;
public:
    Stok()
    {

    }

    Stok(int jumlah, Komputer komputer)
    {
        this->jumlah = jumlah;
        this->komputer = komputer;
    }


    void setJumlah(int jumlah)
    {
        this->jumlah = jumlah;
    }

    void setKomputer(Komputer Komponen)
    {
        this->komputer = komputer;
    }

    int getJumlah()
    {
        return jumlah;
    }

    Komputer getKomputer()
    {
        return this->komputer;
    }

    ~Stok()
    {

    }
};
