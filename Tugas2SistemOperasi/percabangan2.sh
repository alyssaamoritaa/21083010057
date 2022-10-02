#!/bin/bash
printf "Matkul apa yang kamu suka?\n"
printf "Sistem Operasi?\n"
printf "Matematika Diskrit?\n"
printf "Aljabar Linier?\n"
read  Matkul
case "$Matkul" in
"Sistem Operasi")
echo "Soalnya aku suka pakai Linux!"
;;
"Matematika Diskrit")
echo "Menantang, tapi masih ada yang kupahami"
;;
"Aljabar Linier")
echo "Aku suka matkul hitung-hitungan walau matriks bikin pusing"
;;
*)
echo "Gatau deh, baru 3 minggu aja udah pusing banget sama semua matkul"
;;
esac
