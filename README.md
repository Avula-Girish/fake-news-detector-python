# 📰 Fake News Detection using Python 

## 🔍 Overview
This project detects potentially fake news using simple rule-based analysis with **Python, Pandas, and Matplotlib**.

Instead of Machine Learning, it uses heuristic checks such as:

- 🚨 Suspicious word frequency  
- 📏 Headline length analysis  
- 🔠 Capital-letter detection  
- ⚠️ Fake-risk rating system  

It also generates visualizations 📊 and exports results 📁.

---

## ✨ Features

### 1️⃣ Custom Input Mode
Users can enter their own news data:

- 📝 Title  
- 📄 Text  
- 🏷 Subject  

### 2️⃣ Test Dataset Mode
Uses:

- Fake.csv  
- True.csv  

(Default: first 500 rows from each dataset)

---

## 🧠 Detection Logic

Each news article gets a **Fake Rating Score**.

### Rules used:

### 📌 Rule 1: Long Headlines
If title length is greater than average real news title length:

➕ +1 fake score

---

### 📌 Rule 2: Suspicious Fake Keywords
Finds words common in fake news but uncommon in real news.

Examples:

- breaking  
- shocking  
- exposed  
- secret  

If detected:

➕ +1 fake score

---

### 📌 Rule 3: All-Caps Detection
If text is entirely uppercase:

➕ +1 fake score

---

## 🚦 Risk Levels

| Score | Risk Level |
|-------|------------|
| 0 | ✅ Safe |
| 1 | 🟡 Low |
| 2 | 🟠 Moderate |
| 3 | 🔴 High |

---

## 📊 Visualizations

Project generates:

### 📈 Fake Keyword Frequency Chart
Horizontal bar graph of top fake-news words.

### 🥧 Fake Rating Distribution
Pie chart showing:

- ✅ Safe  
- 🟡 Low Risk  
- 🟠 Moderate Risk  
- 🔴 High Risk  

---

## 🛠 Technologies Used

- 🐍 Python  
- 🐼 Pandas  
- 📉 Matplotlib  
- 🔎 Regex (re)

---

## ⚙ Installation

```bash
pip install pandas matplotlib
```

Run:

```bash
python fake_news_detector.py
```

---

## 📁 Output

Results saved as:

```bash
output_results.csv
```

Contains:

- title  
- text  
- rating_fake

---

## 💡 Project Type

Rule-Based NLP Mini Project

---

## 🚀 Future Improvements

- 🤖 Add Machine Learning models  
- 📚 Use TF-IDF  
- 📉 Add Logistic Regression  
- 🌐 Build Streamlit Web App  
- 🎯 Improve fake-news accuracy

---

## 📂 Dataset

Can use commonly available **Fake and True news datasets from Kaggle.**

---

## 👨‍💻 Author

*Girish Avula*
