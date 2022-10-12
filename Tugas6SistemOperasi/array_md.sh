#!/bin/bash

#deklarasi array2dimensi " : " pemisah nilai (array [3][4])
array2dimensi="1.1:1.2:1.3:1.4 2.1:2.2:2.3:2.4 3.1:3.2:3.3:3.4"

#mengakali multi dimensi -> dengan pemisah dimensi "tr :"
function dimensiBaris {
    for baris in $array2dimensi
    do
        dimensiKolom `echo $baris | tr : " "`
    done
}

function dimensiKolom {
    for kolom in $*
    do
        echo -n $kolom " "
    done
    echo
}

#melakukan pemanggilan fungsi
dimensiBaris
