#!/bin/bash

# deklarasi array
distroLinux=("Mint" "Ubuntu" "Kali" "Novell" "Arch")

# random distro
let pilih=$RANDOM%5

# eksekusi
echo "Saya memilih Distro $pilih, ${distroLinux[$pilih]} !"

