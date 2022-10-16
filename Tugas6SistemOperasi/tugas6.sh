#!/bin/bash

echo "Nama : "
read nama

echo "NPM : "
read npm

echo "Jumlah Semester Saat Ini : "
read sem

i=0
sum=0

echo "IP Tiap Semester : "
until [ $i -eq $sem ]
do
   read num
   ips=$((ips + num))
   i=$((i + 1))
done

ipk=$(echo $ips / $sem | bc -l | xargs printf "%.2f")

echo "IPS Mahasiswa = $ips / $sem"
echo "IPK Mahasiswa = $ipk"


