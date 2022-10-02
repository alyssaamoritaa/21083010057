#!?bin/bash

a=15

until [ ! $a -ge 0 ]
do
   echo $a
   a=$((a - 2))
done
