#!/bin/bash

# Mendeklarasikan fungsi
function nama {
    echo "Siapa namamu?"
    read nama
}
function npm {
    echo "Sebutkan npm mu"
    read npm
    echo -e "Hai $nama dengan npm $npm, selamat datang \n di praktikum sistem operasi
yang seru ini ya!"
}

# Memanggil fungsi
nama
npm
