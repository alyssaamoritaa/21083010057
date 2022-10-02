#!/bin/bash
a=22
b=17
if [ $a == $b ]
then
echo "a sama dengan b"
elif [ $a -gt $b ]
then
echo "a lebih besar dari b"
elif [ $a -lt $b ]
then
echo "a lebih kecil dari b"
else
echo "Tidak ada kondisi yang memenuhi"
fi
