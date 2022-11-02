#!/bin/bash

#Mendeklarasikan fungsi
area_rectangle() {
	panjang=$1
	lebar=$2
	let area=$panjang*$lebar
	echo -e  "\nLuas Persegi Panjang : \n$area"
}

echo -e "Masukkan Panjang : "
read p
echo -e "\nMasukkan Lebar : "
read l

#Memanggil fungsi
area_rectangle $p $l $area

