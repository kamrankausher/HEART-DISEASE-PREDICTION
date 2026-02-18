
import streamlit as st
import pandas as pd
import joblib
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Heart Disease Clinical Analyzer",
    page_icon="🩺",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# ---------------- PDF FUNCTION ----------------
def create_medical_report(name, phone, email, risk, level, parameters, advice):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    y = 800
    c.setFont("Helvetica-Bold", 18)
    c.drawString(160, y, "AI Heart Disease Medical Report")

    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Name: {name}")
    y -= 20
    c.drawString(50, y, f"Phone: {phone}")
    y -= 20
    c.drawString(50, y, f"Email: {email}")
    y -= 20
    c.drawString(50, y, f"Date: {datetime.now().strftime('%d %B %Y')}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Clinical Parameters")
    c.setFont("Helvetica", 12)

    for k,v in parameters.items():
        y -= 20
        c.drawString(60, y, f"{k}: {v}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Risk Result: {risk}% ({level})")

    y -= 40
    c.drawString(50, y, "Recommendation")
    c.setFont("Helvetica", 12)
    for line in advice.split("\n"):
        y -= 20
        c.drawString(60, y, line)

    c.save()
    buffer.seek(0)
    return buffer

# ---------------- PREMIUM THEME CSS ----------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"]  {font-family: 'Poppins', sans-serif;}
.stApp {background: linear-gradient(135deg,#06020f,#140a25,#000000);color:white;}
h1, h2, h3 {color:#f5d487;letter-spacing:0.5px;}
p, label {color:white;}
.card {background:rgba(255,255,255,0.04);padding:28px;border-radius:20px;backdrop-filter:blur(16px);
border:1px solid rgba(255,215,120,0.25);box-shadow:0 0 40px rgba(255,215,120,0.12);}
.stButton>button {background:linear-gradient(90deg,#d4af37,#f6e27a);color:black;border-radius:14px;height:3.2em;width:100%;font-size:18px;font-weight:600;border:none;}
.stProgress > div > div > div > div {background-color:#f5d487;}
[data-testid="stMetricValue"] {color:#f5d487;font-size:40px;}
.subtitle {text-align:center;color:#e5e7eb;font-size:16px;}
.section-title {color:#f5d487;margin-bottom:8px;font-weight:600;}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>AI Heart Disease Clinical Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Provide the following details to check your heart stroke risk:</p>", unsafe_allow_html=True)

left, right = st.columns([1.1,1])

# ---------------- INPUT PANEL ----------------
with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Patient Details</div>", unsafe_allow_html=True)

    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")

    st.markdown("<hr style='border:0.5px solid rgba(255,215,120,0.3)'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Clinical Parameters</div>", unsafe_allow_html=True)

    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
    oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PREDICTION LOGIC ----------------
raw_input = {
    'Age': age,'RestingBP': resting_bp,'Cholesterol': cholesterol,'FastingBS': fasting_bs,
    'MaxHR': max_hr,'Oldpeak': oldpeak,'Sex_' + sex: 1,'ChestPainType_' + chest_pain: 1,
    'RestingECG_' + resting_ecg: 1,'ExerciseAngina_' + exercise_angina: 1,'ST_Slope_' + st_slope: 1
}

# ---------------- RESULT PANEL ----------------
with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("AI Diagnosis Report")

    if st.button("Analyze Heart Risk"):

        input_df = pd.DataFrame([raw_input])
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[expected_columns]
        scaled_input = scaler.transform(input_df)

        probability = model.predict_proba(scaled_input)[0][1]
        risk = int(probability * 100)

        st.metric("Predicted Risk Probability", f"{risk}%")
        st.progress(risk/100)

        if risk < 30:
            level="Low Risk"
            advice="Maintain healthy diet\nExercise regularly\nAnnual checkup"
            st.success(f"Low Risk — {name}'s heart condition appears stable.")
        elif risk < 60:
            level="Moderate Risk"
            advice="Reduce cholesterol\nStart cardio exercise\nConsult physician"
            st.warning(f"Moderate Risk — Preventive consultation recommended for {name}.")
        else:
            level="High Risk"
            advice="Immediate cardiologist visit\nECG & Echo test\nMedication required"
            st.error(f"High Risk — Immediate cardiologist consultation advised for {name}.")

        pdf = create_medical_report(
            name, phone, email, risk, level,
            {"Age":age,"BP":resting_bp,"Cholesterol":cholesterol,"MaxHR":max_hr,"Oldpeak":oldpeak},
            advice
        )

        st.download_button(
            "📄 Download Full Medical Report",
            data=pdf,
            file_name=f"{name}_Heart_Report.pdf",
            mime="application/pdf"
        )

    st.markdown("</div>", unsafe_allow_html=True)
