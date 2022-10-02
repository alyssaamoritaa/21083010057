#!/bin/bash
echo "Siapa namamu?"
read nama
echo "Masukkan a: "
read a
echo "Masukkan b: "
read b
echo "Pilihlah salah satu diantara ini!"
echo "Penjumlahan/Pengurangan/Perkalian/Pembagian/Mod"
echo "Pilihanmu : "
read Pilih

case "$Pilih" in
"Penjumlahan")
let hasil=$a+$b
echo "$a+$b = $hasil"
;;
"Pengurangan")
let hasil=$a-$b 
echo "$a-$b = $hasil" 
;; 
"Perkalian")
let hasil=$a*$b 
echo "$a*$b = $hasil" 
;; 
"Pembagian")
let hasil=$a/$b 
echo "$a/$b = $hasil" 
;; 
"Mod")
let hasil=$a%$b 
echo "$a%$b = $hasil" 
;; 
*)
esac
