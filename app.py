import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Dropout Mahasiswa", page_icon="🎓", layout="wide")
st.title("🎓 Jaya Jaya Institut: Student Dropout Predictor")
st.markdown("""
Aplikasi ini menggunakan Machine Learning untuk memprediksi apakah seorang mahasiswa berisiko mengalami **Dropout** atau tidak. 
Silakan masukkan data akademik dan demografi mahasiswa pada form di bawah ini.
""")

@st.cache_resource
def load_model():
    return joblib.load('model/rf_model.joblib')

model = load_model()
with st.form("prediction_form"):
    st.subheader("Data Mahasiswa")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Faktor Demografi & Finansial**")
        age = st.number_input("Usia saat mendaftar (Age_at_enrollment)", min_value=15, max_value=80, value=20)
        gender = st.selectbox("Jenis Kelamin (Gender: 1 = Pria, 0 = Wanita)", [1, 0])
        debtor = st.selectbox("Apakah memiliki hutang? (Debtor: 1 = Ya, 0 = Tidak)", [1, 0])
        tuition = st.selectbox("Status Uang Kuliah (1 = Tepat Waktu, 0 = Menunggak)", [1, 0])
        app_mode = st.number_input("Mode Pendaftaran (Application_mode)", min_value=1, max_value=50, value=1)

    with col2:
        st.markdown("**Faktor Akademik (Semester 1 & 2)**")
        sem1_appr = st.number_input("SKS Semester 1 yang Lulus (Sem 1 Approved)", min_value=0, max_value=20, value=5)
        sem1_grade = st.number_input("Nilai Rata-rata Semester 1 (Sem 1 Grade)", min_value=0.0, max_value=20.0,
                                     value=12.0)
        sem2_appr = st.number_input("SKS Semester 2 yang Lulus (Sem 2 Approved)", min_value=0, max_value=20, value=5)
        sem2_grade = st.number_input("Nilai Rata-rata Semester 2 (Sem 2 Grade)", min_value=0.0, max_value=20.0,
                                     value=12.0)
        sem2_no_eval = st.number_input("Unit Kuliah Sem 2 Tanpa Evaluasi", min_value=0, max_value=15, value=0)

    submit_button = st.form_submit_button("Prediksi Status Mahasiswa")

if submit_button:
    data = {
        'Marital_status': 1, 'Application_mode': app_mode, 'Application_order': 1, 'Course': 1,
        'Daytime_evening_attendance': 1, 'Previous_qualification': 1, 'Previous_qualification_grade': 130.0,
        'Nacionality': 1, 'Mothers_qualification': 19, 'Fathers_qualification': 19,
        'Mothers_occupation': 5, 'Fathers_occupation': 5, 'Admission_grade': 120.0,
        'Displaced': 1, 'Educational_special_needs': 0, 'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition, 'Gender': gender, 'Scholarship_holder': 0,
        'Age_at_enrollment': age, 'International': 0, 'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_enrolled': 6, 'Curricular_units_1st_sem_evaluations': 8,
        'Curricular_units_1st_sem_approved': sem1_appr, 'Curricular_units_1st_sem_grade': sem1_grade,
        'Curricular_units_1st_sem_without_evaluations': 0, 'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_enrolled': 6, 'Curricular_units_2nd_sem_evaluations': 8,
        'Curricular_units_2nd_sem_approved': sem2_appr, 'Curricular_units_2nd_sem_grade': sem2_grade,
        'Curricular_units_2nd_sem_without_evaluations': sem2_no_eval, 'Unemployment_rate': 11.1,
        'Inflation_rate': 0.6, 'GDP': 0.32
    }

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    st.divider()
    if prediction == 1:
        st.error("### 🚨 Peringatan: Mahasiswa ini berisiko tinggi untuk DROPOUT.")
        st.markdown("Rekomendasi: Segera jadwalkan sesi konseling akademik dan periksa status finansialnya.")
    else:
        st.success("### ✅ Aman: Mahasiswa ini diprediksi akan LULUS (Graduate).")
        st.markdown("Rekomendasi: Terus pantau dan pertahankan performa akademiknya.")