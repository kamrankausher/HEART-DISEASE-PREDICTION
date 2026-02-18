# 🩺 AI Heart Disease Clinical Analyzer

A professional Machine Learning powered web application that predicts the risk of heart disease using clinical parameters and generates a downloadable medical report.

Built using **Python, Scikit-Learn and Streamlit**, this system simulates a real clinical decision-support tool used in healthcare environments.

---

## 🌐 Live Application

> *(Add your Streamlit deployment link here after hosting)*

---

## 📌 Project Overview

Cardiovascular diseases are one of the leading causes of death worldwide.
This project aims to assist in **early screening and preventive diagnosis** by analyzing patient health parameters using a trained ML model.

The application:

* Accepts patient clinical inputs
* Predicts heart disease risk probability
* Classifies risk level (Low / Moderate / High)
* Provides preventive medical advice
* Generates a downloadable PDF medical report

---

## 🧠 Machine Learning Details

**Algorithm Used:** K-Nearest Neighbors (KNN)
**Problem Type:** Binary Classification
**Target:** Presence of Heart Disease

### Features Used

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Max Heart Rate
* Exercise Induced Angina
* Oldpeak (ST Depression)
* ST Slope

---

## 🖥️ Application Features

### Clinical Prediction

* Real-time risk prediction
* Probability based output
* Risk level interpretation

### Patient Interface

* Modern medical themed UI
* Patient personal details input
* Interactive parameter selection

### Medical Report Generation

* Downloadable PDF report
* Includes all patient parameters
* Risk percentage and category
* Preventive recommendations
* Date & AI diagnosis header

---

## 🛠️ Tech Stack

| Category            | Technology    |
| ------------------- | ------------- |
| Language            | Python        |
| ML Library          | Scikit-Learn  |
| Web Framework       | Streamlit     |
| Data Handling       | Pandas, NumPy |
| Model Serialization | Joblib        |
| Report Generation   | ReportLab     |

---

## 📂 Project Structure

```
heart-disease-predictor/
│── app.py
│── KNN_heart.pkl
│── scaler.pkl
│── columns.pkl
│── heart.csv
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/heart-disease-predictor.git
cd heart-disease-predictor
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📊 Model Workflow

1. User enters patient details
2. Input is converted into encoded feature vector
3. Data is scaled using trained scaler
4. KNN model predicts probability
5. Risk category determined
6. Medical report generated

---

## 🎯 Future Improvements

* Explainable AI (feature importance)
* Doctor login dashboard
* Database storage of reports
* Email report to patient
* Multi-disease prediction system

---

## ⚠️ Disclaimer

This system is for **educational and screening purposes only** and should not replace professional medical diagnosis.

---

## 👨‍💻 Author

**Kamran Kausher**
B.Tech CSE | Aspiring AI/ML Engineer

---
