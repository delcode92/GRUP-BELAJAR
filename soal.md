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




### 3) buat program yang bisa mengurutkan skor siswa (dari yang paling besar, ke paling kecil) dalam sebuah dictionary

case 1:
input dictionary --> { "ani":80, "budi":70, "ana":55, "susi":75, "rudi":60 }

output --> urutan skor siswa:
	ani -> 80
	susi -> 75
	budi -> 70
	rudi -> 60
	ana -> 55





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




### 5) buat function yang bisa mencari nilai tengah dalam sebuah list (bilangan berupa integer)

#### case 1:
input--> [10, 12, 18, 19, 21, 23]
output --> 18.5


#### case 2:
input--> [13, 17, 18, 21, 23]
output --> 18





### 6) buat function yang bisa mencari nilai rata-rata dari sebuah list (bilangan berupa integer)

#### case 1:
input--> [10, 12, 18, 19, 21, 23]
output --> 17.16


#### case 2:
input--> [13, 17, 18, 21, 23]
output --> 18.4






### 7) buat function yang bisa group data dalam sebuah list (artinya remove data yg duplicate sisakan satu)

#### case 1:
input--> [10, 12, 18, 19, 21, 18, 23] 
output --> [10, 12, 18, 19, 21, 23] --> nilai 18 yg awalnya 2 buah data di remove duplicate nya, sisakan satu aja



#### case 2:
input--> [13, 17, 18, 21,13, 13, 23, 17, 18]
output --> [13, 17, 18, 21, 23] --> nilai 13, 17 dan 18 di remove duplicate nya 





### 8) buat function yang bisa menentukan nilai apa yang paling sering muncul dalam sebuah list (nilai dalam bentuk integer)

#### case 1:
input--> [10, 12, 18, 19, 10, 21, 18, 23, 10] 
output --> 10 , muncul sebanyak 3 kali



#### case 2:
input--> [10, 23, 12, 18, 23,19, 10, 21, 18, 23, 10] 
output --> 23 dan 10 , muncul sebanyak 3 kali