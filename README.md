Pasaran
=======

Saya tinggal di kampung yang rapat RT-nya ditentukan berdasar pasaran, kami mengadakan pertemuan tiap malam Selasa Kliwon. Permasalahannya, saya malas pasang kalender di dinding. Akibatnya, 3 kali saya terlewat rapat RT.

Maka saya bikinlah script ini, biar saya bisa cek tiap hari, saat ini pasarannya apa.

Kalau ada kritik saran, monggo.

Mac Apps
========
Dengan menggunakan `rumps` dan `py2app` saya generate script pasaran ini menjadi apps. Semoga berguna. :)

Tambahan
========
Saya menambahkan weton.py yang fungsinya untuk mencari:
- weton untuk tanggal tertentu, misalnya mencari pasaran tanggal 20-12-2013
- geblak. untuk mencari tanggal 3 dina, 7 dina, 40 dina dan seterusnya, biasanya perhitungan ini dipakai untuk menentukan kapan orang jawa melakukan selamatan terkait dengan meninggalnya seseorang. untuk menggunakan fungsi ini, anda cukup memasukkan tanggal kematian orang tersebut.
- pasaran. untuk mencari kombinasi hari dan pasaran dalam setahun. untuk ini anda tinggal memasukkan kombinasi misalnya "senin wage" atau "selasa kliwon" atau "kamis pahing" dan seterusnya.

ASCII Art
==========
[06-07-2018] Saya tambahkan ascii art, menampilkan gambar wayang batara/dewa yang menaungi ketika melakukan pencarian wuku. ASCII art saya ambil dari `asciisciit` dengan penyesuaian beberapa file agar bisa berjalan di python3.

Jalankan `pip install -r asciisciit/requirements.txt` agar bisa menampilkan gambar wayang dalam format ascii art.

Penggunaan
==========

    $ python pasaran.py
    Saiki malem Septu Pon

    ## untuk menampilkan help
    $ python weton.py -h

    ## untuk mencari weton
    $ python weton.py -w 20-12-1983
    Tanggal 20-12-1983 iku nagadinane Seloso Kliwon

    ## untuk mencari geblak
    $ python weton.py -g 20-01-1984
    Geblake jenat: 20-12-1984, Kemis Legi
    Telung dinane jenat: 22-12-1984, Septu Pon
    Pitung dinane jenat: 26-12-1984, Rebo Pahing
    ...

    ## untuk mencari pasaran
    $ python weton.py -p "jumat kliwon"
    Mencari pasaran di Tahun:
    2013
    jumat kliwon (0) :11-01-2013
    jumat kliwon (1) :15-02-2013
    jumat kliwon (2) :22-03-2013
    ...

    ## untuk mencari pawukon
    $ python weton.py -pw "20-9-1906"
    20 September 1906 iku dino Kemis Kliwon, wuku: Wukir

Rujukan
========
- Tiga Cara Menentukan Nama Wuku Dalam Pawukon Saka  (https://jmpunsoed.files.wordpress.com/2015/12/4-agung-sugiyanto-indar1.pdf)
- ASCII ART (https://github.com/derricw/asciisciit)
