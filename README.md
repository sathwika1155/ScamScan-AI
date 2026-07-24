<div align="center">

# 🛡️ ScamScan-AI

### AI-Powered Scam Message Detection using Machine Learning, Flask & Streamlit

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=24&pause=1000&color=2E8B57&center=true&vCenter=true&width=600&lines=Detect+Scam+Messages+Instantly;Machine+Learning+Powered;Flask+API+%2B+Streamlit+Frontend;Hackathon+Project" />

---

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data-purple?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

</div>

---

# 📌 Overview

**ScamScan-AI** is an intelligent Machine Learning application that detects scam messages, phishing emails, and suspicious text using Natural Language Processing (NLP).

Users simply paste a message into the web application, and the model predicts whether it is **Scam** or **Not Scam**, along with a confidence score.

The project demonstrates a complete Machine Learning pipeline—from data preprocessing and model training to API development and frontend deployment.

---

# 🎯 Problem Statement

Scam messages and phishing emails have become one of the most common cyber threats worldwide.

Millions of users receive fake messages such as:

- Lottery scams
- Bank verification scams
- Fake delivery notifications
- OTP scams
- Job offer scams
- Investment fraud

Many users cannot easily distinguish between genuine and fraudulent messages.

ScamScan aims to provide a simple AI-powered solution for detecting such scams instantly.

---

# 💡 Our Solution

ScamScan uses Machine Learning to classify text messages into:

✅ Scam

❌ Not Scam

using

- TF-IDF Vectorization
- Logistic Regression Classification

The prediction is returned through a Flask API and displayed in a clean Streamlit interface.

---

# ✨ Features

✅ Scam Message Detection

✅ Email Scam Detection

✅ Confidence Score

✅ Machine Learning Prediction

✅ Flask REST API

✅ Interactive Streamlit UI

✅ Beginner-Friendly Architecture

✅ Easy Deployment

---

# 🏗 Project Architecture

```text
                    User

                      │

                      ▼

          Streamlit Frontend (UI)

                      │

          POST Request (JSON)

                      │

                      ▼

              Flask REST API

                      │

          Load Saved ML Model

                      │

             TF-IDF Vectorizer

                      │

        Logistic Regression Model

                      │

          Prediction + Confidence

                      │

                      ▼

            Display Result to User
```

---

# 📂 Project Structure

```text
ScamScan-AI
│
├── backend
│      app.py
│      requirements.txt
│
├── frontend
│      app.py
│      requirements.txt
│
├── model
│      scam_model.pkl
│      vectorizer.pkl
│
├── notebook
│      ScamScan_Model_Training.ipynb
│
├── data
│      spam_cleaned.csv
│
├── report
│      ScamScan_Report.pdf
│
├── README.md
│
└── LICENSE
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Processing |
| Scikit-Learn | Machine Learning |
| TF-IDF | Feature Extraction |
| Logistic Regression | Classification |
| Joblib | Save ML Model |
| Flask | Backend API |
| Streamlit | Frontend UI |
| GitHub | Version Control |
| Render | Backend Deployment |
| Streamlit Cloud | Frontend Deployment |

---

# 📊 Machine Learning Workflow

```text
Dataset

↓

Cleaning

↓

Label Encoding

↓

Train-Test Split

↓

TF-IDF Vectorization

↓

Model Training

↓

Evaluation

↓

Save Model

↓

Flask API

↓

Streamlit Interface
```

---

# 📈 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | 98%+ |
| Precision | High |
| Recall | High |
| F1 Score | High |

*(Values depend on the dataset and training.)*

---


# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/yourusername/ScamScan-AI.git
```

Go to Project

```bash
cd ScamScan-AI
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Flask Backend

```bash
cd backend

python app.py
```

Run Streamlit Frontend

```bash
cd frontend

streamlit run app.py
```

---

# 🌐 Deployment

### Backend

Render

### Frontend

Streamlit Cloud

---

# 📊 Dataset

Dataset Used

SMS Spam Collection Dataset

Contains

- Spam Messages
- Genuine Messages

Columns

```
label

text
```

---

# 🔄 API Endpoint

POST

```
/predict
```

Input

```json
{
"text":"Congratulations! You won ₹5,00,000."
}
```

Output

```json
{
"prediction":"Scam",
"confidence":99.42
}
```

---

# 🚀 Future Enhancements

- 🌍 Multilingual Scam Detection

- 📱 Android Application

- 🌐 Chrome Extension

- 🔗 URL Phishing Detection

- 📧 Email Attachment Scanner

- 💬 WhatsApp Scam Detection

- 🤖 AI Chatbot Assistant

- 🔊 Voice Scam Detection

- 📸 OCR for Image-based Scams

---

# 🎯 Hackathon Highlights

✔ End-to-End ML Project

✔ REST API Development

✔ Interactive Web Interface

✔ Real-Time Prediction

✔ Cloud Deployment Ready

✔ Modular Architecture

✔ Beginner Friendly

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a new branch

3. Commit your changes

4. Push the branch

5. Open a Pull Request

---

# 👩‍💻 Author

**Sathwika Reddy**

Data Science Student

Machine Learning Enthusiast

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub!

It motivates future development and improvements.

---

<div align="center">

### Made with ❤️ using Python, Flask, Streamlit & Machine Learning

</div>
