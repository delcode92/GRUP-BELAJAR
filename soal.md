## soal:

### 1) buat program yang bisa mencari jumlah bilangan genap, dalam sebuah list & tampilkan angka-angka nya

### case 1:
input list --> [1, 3, 6, 8, 11]

output(level 1) --> bilangan genap dalam list ada 2 buah, yaitu 6,8

output(level 2) --> bilangan genap dalam list ada 2 buah, yaitu 6 dan 8

### Note: 
untuk output level 2 menggunakan kata "dan" jika jumlah bilangan lebih daripada satu

_________________________________________________________________________________________________________________________________


### 2) buat program yang bisa mencari jumlah bilangan ganjil, dalam sebuah list & tampilkan angka-angka nya

case 1:
input list --> [1, 3, 6, 8, 11]

output( level 1 ) --> bilangan ganjil dalam list ada 3 buah, yaitu 1,3,11

output( level 2 ) --> bilangan ganjil dalam list ada 3 buah, yaitu 1,3 dan 11

*Note: 
untuk output level 2 menggunakan kata "dan" jika jumlah bilangan lebih daripada satu

_________________________________________________________________________________________________________________________________



### 3) buat program yang bisa mengurutkan skor siswa (dari yang paling besar, ke paling kecil) dalam sebuah dictionary

case 1:
input dictionary --> { "ani":80, "budi":70, "ana":55, "susi":75, "rudi":60 }

output --> urutan skor siswa:
	ani -> 80
	susi -> 75
	budi -> 70
	rudi -> 60
	ana -> 55


_________________________________________________________________________________________________________________________________



### 4) buat function bonus() yang  memiliki 2 argument  --->  def bonus(salary, bonus):

salary --> nilainya berupa integer
bonus --> nilainya berupa boolean

jika bonus==True maka, nilai salary dikalian dengan 10
jika bonus==False, maka tidak ada bonus

case 1:

bonus(500, True) 
output: bonus sebesar 5000




case 2:

bonus(1200, True) 
output: bonus sebesar 12000




case 3:

bonus(1200, False) 
output: Tidak ada bonus

_________________________________________________________________________________________________________________________________



### 5) buat function yang bisa mencari nilai tengah dalam sebuah list (bilangan berupa integer)

#### case 1:
input--> [10, 12, 18, 19, 21, 23]
output --> 18.5


#### case 2:
input--> [13, 17, 18, 21, 23]
output --> 18


_________________________________________________________________________________________________________________________________


### 6) buat function yang bisa mencari nilai rata-rata dari sebuah list (bilangan berupa integer)

#### case 1:
input--> [10, 12, 18, 19, 21, 23]
output --> 17.16


#### case 2:
input--> [13, 17, 18, 21, 23]
output --> 18.4


_________________________________________________________________________________________________________________________________



### 7) buat function yang bisa group data dalam sebuah list (artinya remove data yg duplicate sisakan satu)

#### case 1:
input--> [10, 12, 18, 19, 21, 18, 23] 
output --> [10, 12, 18, 19, 21, 23] --> nilai 18 yg awalnya 2 buah data di remove duplicate nya, sisakan satu aja



#### case 2:
input--> [13, 17, 18, 21,13, 13, 23, 17, 18]
output --> [13, 17, 18, 21, 23] --> nilai 13, 17 dan 18 di remove duplicate nya 


_________________________________________________________________________________________________________________________________



### 8) buat function yang bisa menentukan nilai apa yang paling sering muncul dalam sebuah list (nilai dalam bentuk integer)

#### case 1:
input--> [10, 12, 18, 19, 10, 21, 18, 23, 10] 
output --> 10 , muncul sebanyak 3 kali



#### case 2:
input--> [10, 23, 12, 18, 23,19, 10, 21, 18, 23, 10] 
output --> 23 dan 10 , muncul sebanyak 3 kali

_________________________________________________________________________________________________________________________________


### 9) buat program yang bisa menampilkan dan menghitung nilai faktorial

#### case 1:
input--> 5
output --> faktorialnya 1x2x3x4x5= 120


________________________________________________________________________________________________________________________________


### 10) buat program yang bisa menghandle conflict dari atom yang digabungkan

#### problem:
pada sebuah lab kimia yang membuat bahan peledak, terdapat beberapa atom/unsur kimia yg boleh digabungkan/dicampur dan ada atom yg tidak boleh dicampur. Jika dua/lebih dari bahan tersebut dicampur, maka akan terjadi reaksi spontan yg dapat menyebabkan ledakan yg tidak terkendali

#### yg tidak boleh digabung:
Pb -> B, Si, Sb, Te, Pd <br>
Re -> Ti, Db, Si<br>
Ac -> La, Fr, K, Db<br>

buat program yang dapat memberikan peringatan jika ada elemen/unsur kimia yg tidak boleh digabung

#### case 1:
input--> [Pb, Re, Db, Si, La]

#### output: 
Pb tidak boleh digabung dengan Si<br>
Re tidak boleh digabung dengan Db<br>
Re tidak boleh digabung dengan Si<br>

#### case 2:
input--> [K, Fr, Re, B, Pb]

#### output: 
B tidak boleh digabung dengan Pb

________________________________________________________________________________________________________________________________


### 11) buat program translate kata sederhana kedalam bahasa inggris menggunakan python

#### case 1:
input  --> hello

output --> hello


#### case 2:
input  --> cuaca

output --> weather

________________________________________________________________________________________________________________________________



### 12) buat program translate kata sederhana menggunakan python, tapi user bisa pilih dia mau translate ke indonesia - inggris atau inggris -indonesia

#### case 1:
pilih bahasa:
1. indonesia = inggris
2. inggris - indonesia

-->1

input  --> hello
output --> hello


#### case 2:

pilih bahasa:
1. indonesia = inggris
2. inggris - indonesia

-->2


input  --> weather
output --> cuaca



________________________________________________________________________________________________________________________________



### 13) buat program manipulasi string berdasarkan input dan output yg diperintahkan <span id="manipulasi_string"/>

#### 1. ubah format tanggal :

#### case 1 ( year/month/date to date/month/year):

input --> 1990/02/25
output --> 25/02/1990


#### case 2 ( year/month/date to date-month-year):

input --> 1990/02/25
output --> 25-02-1990

--------------------------------------------------

#### 2. ganti angka 0 pada awalan nomor HP menjadi +62 :

input --> 085260346325
output --> +6285260346325

--------------------------------------------------

#### 3. print angka yg terdapat setelah prefix berikut :

#### case 1 (prefix: - ) :
input --> PT-10
output --> 10


#### case 1 (prefix: # ) :
input --> KD#205
output --> 205

----------------------------------------------------

#### 4. buang semua spasi kecuali pemisah antar kata:

#### case 1:
input -->                  ular melingkar dipagar pak umar                  
output --> ular melingkar dipagar pak umar

#### case 2:
input -->                  ular               melingkar dipagar          pak                umar                  
output --> ular melingkar dipagar pak umar

----------------------------------------------------

#### 5. keluarkan data yang diminta, dari JSON atau dictionary berikut:

#### case 1:
#### data ---> {"siswa-1":{"nama":"Budi", "alamat":"pango", "hp":"12345", "jk":"laki-laki"}}

input --> alamat
output --> pango
