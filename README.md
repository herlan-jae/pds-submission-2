# Student Performance & Dropout Detection - Jaya Jaya Institut

## 1. Latar Belakang Bisnis
Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan mencetak banyak lulusan bereputasi baik. Namun, saat ini institusi menghadapi tantangan serius berupa tingginya angka mahasiswa yang tidak menyelesaikan pendidikannya alias *dropout*. Jika dibiarkan, rasio *dropout* yang tinggi ini akan berdampak buruk pada reputasi akademik institusi dan stabilitas finansial operasional kampus.

---

## 2. Permasalahan Bisnis
Berdasarkan latar belakang tersebut, Jaya Jaya Institut perlu menyelesaikan permasalahan berikut:
1. Mengidentifikasi faktor-faktor demografi, finansial, dan akademik yang memicu tingginya tingkat *dropout* mahasiswa.
2. Membangun sebuah *business dashboard* interaktif untuk memonitor performa dan status mahasiswa secara *real-time*.
3. Membuat prototype sistem prediksi berbasis *Machine Learning* untuk mengidentifikasi mahasiswa baru atau mahasiswa aktif yang memiliki probabilitas tinggi untuk *dropout*, sehingga pihak kampus dapat memberikan bimbingan khusus sedini mungkin.

---

## 3. Cakupan Proyek
Proyek analisis data dan *machine learning* ini mencakup tahapan *end-to-end* berikut:
* **Data Understanding & Preparation:** Memuat dataset, membersihkan data dengan menyisihkan status mahasiswa 'Enrolled', dan melakukan *encoding* pada target klasifikasi (Dropout = 1, Graduate = 0).
* **Exploratory Data Analysis (EDA):** Menganalisis korelasi (*Pearson Correlation*) antara variabel target dengan 36 fitur lainnya untuk menemukan *insight* faktor pendorong dan penahan *dropout*.
* **Business Dashboard Development:** Mendesain *dashboard* menggunakan Metabase yang terhubung dengan database SQLite (`jaya_jaya.db`).
* **Machine Learning Modeling:** Mengembangkan model klasifikasi menggunakan algoritma **Random Forest Classifier** yang dievaluasi menggunakan *Confusion Matrix* dan *Classification Report*.
* **Deployment Prototype:** Membuat antarmuka aplikasi interaktif menggunakan **Streamlit** (`app.py`) yang memuat model terlatih untuk memprediksi risiko *dropout* berdasarkan input data mahasiswa.

---

## 4. Sumber Data
Dataset yang digunakan dalam proyek ini mencakup informasi komprehensif terkait demografi, riwayat akademik sebelumnya, status finansial, dan performa akademik mahasiswa di semester 1 dan 2.
Tautan Dataset: (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

---

## 5. Setup Environment & Menjalankan Prototype (Streamlit)
Aplikasi prototype dijalankan menggunakan environment **Conda**. Berikut cara menjalankannya di *local environment*:

**Langkah Instalasi & Eksekusi:**
1. Buka terminal dan arahkan ke direktori proyek (`pds-submission-2`).
2. Aktivasi *environment* Conda:
   ```
   conda activate submission_env
   ```
3. Instal dependencies (jika belum):
   ```
   pip install -r requirements.txt
   ```
4. Jalankan prototype Streamlit:
   ```
   streamlit run app.py
   ```
5. Akses aplikasi melalui browser pada URL http://localhost:8501.

---

## 6. Business Dashboard (Metabase)
Untuk memudahkan institusi dalam memonitor faktor penentu dropout, sebuah dashboard berjudul "Jaya Jaya Student Performance Dashboard" telah dibangun. (Screenshot terlampir pada direktori herlanjae-dashboard).
Berikut adalah fitur visualisasi beserta insight yang diperoleh:
1. Proporsi Mahasiswa (Lulus vs Dropout) (Pie Chart)
   - Insight: Rasio dropout menyentuh angka sekitar 39%. Angka ini sangat tinggi dan mengonfirmasi adanya masalah retensi mahasiswa yang serius di institusi.

2. Pengaruh Keteraturan Bayar Uang Kuliah (Bar Chart)
   - Insight: Keteraturan membayar uang kuliah (Tuition_fees_up_to_date) adalah faktor penahan dropout terkuat. Mahasiswa yang menunggak memiliki lonjakan rasio dropout yang sangat ekstrem dibandingkan yang membayar tepat waktu.

3. Risiko Dropout pada Mahasiswa Berhutang (Bar Chart)
   - Insight: Kepemilikan hutang (Debtor) berkorelasi positif kuat dengan kegagalan studi. Mahasiswa dengan hutang jauh lebih rentan untuk tidak menyelesaikan pendidikannya.

4. Tren Dropout Berdasarkan Usia Pendaftaran (Line Chart)
   - Insight: Usia saat mendaftar (Age_at_enrollment) menunjukkan tren bahwa semakin tua usia mahasiswa saat pertama kali mendaftar, semakin besar pula risiko mereka untuk dropout di tengah jalan.

## 7. Konklusi
Ketiga permasalahan bisnis utama Jaya Jaya Institut telah berhasil diselesaikan:
1. Identifikasi Faktor: Melalui EDA, ditemukan bahwa beban finansial (hutang dan tunggakan uang kuliah) serta usia pendaftaran yang lebih tua adalah pemicu utama dropout. Sebaliknya, performa akademik yang baik di 2 semester awal (SKS lulus & nilai tinggi) menjamin mahasiswa untuk lulus.
2. Monitoring Terpusat: Dashboard Metabase telah berhasil mendemonstrasikan perbandingan langsung antara mahasiswa yang lulus dan dropout berdasarkan faktor-faktor krusial tersebut, memberikan pandangan mata elang bagi manajemen kampus.
3. Prediksi Proaktif: Model Machine Learning Random Forest berhasil dilatih dengan tingkat akurasi mencapai 92.84% dan Precision untuk mendeteksi kelas Dropout sebesar 94%. Model ini telah sukses diintegrasikan ke dalam antarmuka Streamlit yang mudah digunakan.

## 8. Rekomendasi Action Items
Berdasarkan hasil analisis, berikut adalah rekomendasi strategis untuk Jaya Jaya Institut:
1. Peringatan Dini & Bantuan Finansial: Karena tunggakan uang kuliah dan status hutang adalah pemicu utama dropout, pihak kampus harus segera memanggil mahasiswa yang mulai menunggak di semester awal untuk sesi konseling. Tawarkan opsi restrukturisasi cicilan, keringanan biaya, atau program beasiswa internal agar mereka tidak putus asa secara finansial.
2. Program Pendampingan Mahasiswa Dewasa: Mahasiswa yang mendaftar di usia yang lebih tua memiliki tingkat dropout lebih tinggi. Kampus perlu menyediakan layanan orientasi khusus atau metode pembelajaran yang lebih fleksibel (blended learning) untuk mengakomodasi mahasiswa yang mungkin membagi waktu antara kuliah dan bekerja.
3. Fokus Intervensi Akademik di Tahun Pertama: Pantau ketat SKS yang lulus dan nilai IPK pada Semester 1 dan 2. Sistem akademik harus otomatis mengirimkan notifikasi kepada Dosen Wali jika mahasiswa gagal melampaui standar nilai tertentu di tahun pertamanya.
4. Adopsi Sistem Prediksi Streamlit: Petugas administrasi pendaftaran dan Dosen Wali sangat disarankan menggunakan aplikasi Streamlit yang telah dibuat untuk memasukkan profil profil mahasiswa baru, sehingga langkah pencegahan bisa dilakukan bahkan sebelum mahasiswa tersebut menunjukkan tanda-tanda penurunan nilai.