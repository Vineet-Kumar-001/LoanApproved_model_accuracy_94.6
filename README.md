# Loan Approved Prediction System 🚀

## 🐳 Run using Docker

Pull the image:

```bash
docker pull vineetkumar001/loanapproved:latest
```

Run the container:

```bash
docker run -p 8000:8000 -p 8501:8501 vineetkumar001/loanapproved:latest
```

Now open:

http://localhost:8501



## 📌 Project Overview

This project is an end-to-end Machine Learning system that predicts whether a loan application will be approved or not. The model achieves **94.6% accuracy** using a structured ML pipeline and is deployed using FastAPI, Streamlit, and Docker.

The system includes:

* Data preprocessing pipeline
* Model training and evaluation
* REST API using FastAPI
* Frontend UI using Streamlit
* Dockerized deployment

---

## 🧠 Machine Learning Workflow

### 1️⃣ Data Preprocessing

* Handling missing values using SimpleImputer
* Encoding categorical variables (One-Hot Encoding / Label Encoding)
* Feature scaling using StandardScaler
* ColumnTransformer for combining pipelines

### 2️⃣ Model

* K-Nearest Neighbors (KNN) Classifier
* Hyperparameter tuning
* Final model serialized using Pickle

### 3️⃣ Model Performance

* Accuracy: **94.6%**
* Evaluated using train-test split

---

## 🏗️ Project Structure

```
LoanApproved_model_accuracy_94.6/
│
├── app/
│   ├── api.py
│   ├── schema.py
│
├── model/
│   ├── full_system_new.pkl
│
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository

```
git clone https://github.com/Vineet-Kumar-001/LoanApproved_model_accuracy_94.6.git
cd LoanApproved_model_accuracy_94.6
```

### 🔹 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 🔹 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🚀 Run the Application

### ▶️ Run FastAPI Server

```
uvicorn app.api:app --reload
```

API will run on:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

### ▶️ Run Streamlit Frontend

```
streamlit run streamlit_app.py
```

---

## 🐳 Docker Deployment

### 🔹 Build Docker Image

```
docker build -t loanapproved .
```

### 🔹 Run Container

```
docker run -p 8000:8000 loanapproved
```

---

## 🧪 Example API Request

### POST /predict

Example JSON Input:

```
{
  "gender": "Male",
  "married": "Yes",
  "dependents": 0,
  "education": "Graduate",
  "self_employed": "No",
  "applicant_income": 5000,
  "coapplicant_income": 2000,
  "loan_amount": 150,
  "loan_term": 360,
  "credit_history": 1,
  "property_area": "Urban"
}
```

Response:

```
{
  "loan_status": "Approved"
}
```

---

## 📦 Tech Stack

* Python
* Scikit-learn
* Pandas
* FastAPI
* Streamlit
* Docker

---

## 👨‍💻 Author

Vineet Kumar

---

## ⭐ If you found this project useful

G
