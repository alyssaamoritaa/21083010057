#!/bin/bash

# Mendeklarasikan fungsi
nama() {
    echo "Siapa namamu?"
    read nama
    npm                              # <------ Memanggil fungsi di dalam fungsi
}
npm() {
   echo "Sebutkan npm mu"
   read npm
   echo -e "Hai $nama dengan npm $npm, selamat datang \n di praktikum sistem operasi
yang seru ini ya!"
}

# Memanggil fungsi
nama
