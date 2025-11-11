# 📡 Discrete Fourier Transform (DFT) & Spektrogram

---

## 1. Discrete Fourier Transform (DFT)

Discrete Fourier Transform (DFT) merupakan metode yang digunakan untuk mengubah sinyal dari domain waktu menjadi domain frekuensi sehingga kita dapat mengetahui frekuensi-frekuensi penyusun suatu sinyal.  Pada suara manusia, DFT digunakan untuk mengidentifikasi frekuensi fundamental dan formant yang mencirikan vokal serta intonasi seseorang, sehingga banyak dimanfaatkan dalam sistem pengenalan suara (speech recognition) dan analisis kualitas vokal. Dalam suara alam, seperti suara hujan, DFT membantu memisahkan dan mengenali pola frekuensi yang khas dari setiap sumber suara, sehingga berguna dalam penelitian bioakustik dan pemantauan lingkungan. Sementara itu, pada suara musik, DFT memungkinkan analisis komponen harmonik dari setiap nada, mendeteksi tempo dan akor, serta menjadi dasar bagi aplikasi pengolahan audio digital seperti equalizer, auto-tuning, dan music information retrieval. Dengan demikian, DFT berperan penting dalam memahami dan mengolah berbagai bentuk sinyal suara berdasarkan karakteristik frekuensinya.

### 🔹 Persamaan DFT

![DFT](https://latex.codecogs.com/png.image?\dpi{120}\bg{white}X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi%20kn/N})

### 🔹 Bentuk Bilangan Kompleks

![complex](https://latex.codecogs.com/png.image?\dpi{120}\bg{white}X[k]=Re(X[k])+jIm(X[k]))

### 🔹 Magnitudo dan Fase

![magnitude](https://latex.codecogs.com/png.image?\dpi{120}\bg{white}|X[k]|=\sqrt{Re(X[k])^2+Im(X[k])^2})

![phase](https://latex.codecogs.com/png.image?\dpi{120}\bg{white}\phi[k]=\tan^{-1}\left(\frac{Im(X[k])}{Re(X[k])}\right))

### 🔹 Resolusi Frekuensi

![res](https://latex.codecogs.com/png.image?\dpi{120}\bg{white}\Delta%20f%20%3D%20%5Cfrac%7Bf_s%7D%7BN%7D)

> Semakin besar N, resolusi frekuensi semakin baik.

---

## 2. Short Time Fourier Transform (STFT)

DFT dilakukan per segmen menggunakan window untuk menangkap perubahan frekuensi terhadap waktu.

### 🔹 Persamaan STFT

![STFT](https://latex.codecogs.com/png.image?\dpi{120}\bg{white}X(m,k)=\sum_{n=0}^{N-1}x[n]w[n-m]e^{-j2\pi%20kn/N})

---

## 3. Spektrogram

Spektrogram merupakan representasi visual dari distribusi energi atau amplitudo sinyal terhadap waktu dan frekuensi, yang dihasilkan melalui proses Short-Time Fourier Transform (STFT). Dalam metode ini, sinyal dibagi menjadi beberapa segmen waktu pendek (windowing), kemudian masing-masing segmen dianalisis menggunakan Discrete Fourier Transform (DFT) untuk memperoleh informasi spektral pada interval waktu tertentu. Hasil dari proses tersebut divisualisasikan dalam bentuk grafik dua dimensi, di mana sumbu horizontal menunjukkan waktu, sumbu vertikal menunjukkan frekuensi, dan intensitas warna menggambarkan amplitudo atau daya sinyal. Dengan demikian, spektrogram memungkinkan analisis sinyal non-stasioner, yaitu sinyal yang karakteristik frekuensinya berubah terhadap waktu, yang tidak dapat ditangkap secara optimal oleh transformasi Fourier biasa.

![spec](https://latex.codecogs.com/png.image?\dpi{120}\bg{white}Spectrogram(m,k)=|X(m,k)|^2)

### Cara membaca:
| Sumbu / Elemen | Arti |
|---|---|
| X | Waktu |
| Y | Frekuensi |
| Warna | Intensitas energi |

---

## 4. DFT vs Spektrogram

| Fitur | DFT | Spektrogram |
|---|---|---|
| Informasi waktu | ❌ Tidak Ada | ✅ Ada |
| Informasi frekuensi | ✅ Ada | ✅ Ada |
| Output | 1D | 2D (t vs f) |

---

## 5. Kesimpulan

DFT menunjukkan *frekuensi apa saja, tetapi tidak **kapan munculnya. STFT mengatasi hal ini dengan menganalisis sinyal per segmen, lalu divisualisasikan sebagai spektrogram untuk melihat **waktu vs frekuensi vs energi*.
