# 🧠 Personality Type Classification

## 📌 Project Description

This project classifies individuals as **Introverts**, **Extroverts**, or **Ambiverts** using a personality trait dataset and machine learning techniques. It is part of the **SOFTDSNL course prelims** and focuses on exploring behavioral data to understand social dynamics through classification models.

---

## 📊 Dataset Description

**Dataset:** [Introvert, Extrovert & Ambivert Classification](https://www.kaggle.com/datasets/miadul/introvert-extrovert-and-ambivert-classification)

The dataset contains responses from a psychological survey intended to identify social behavior types. It includes several behavioral indicators, such as:

- Time spent with others  
- Comfort in social settings  
- Decision-making style  
- Preference for solitude or teamwork  

Each record ends with a `personality_type` label:  
**["Introvert", "Extrovert", "Ambivert"]**

---

## 🧾 Features and Target

### 🔍 Features (Selected)

| Feature Name               | Description                                     |
|----------------------------|-------------------------------------------------|
| `talking_often`            | How often the person talks to others           |
| `comfortable_large_groups`| Comfort level in large groups                  |
| `likes_solitude`           | Preference for alone time                      |
| `decision_thoughtful`      | Tendency to make decisions after thinking      |
| `likes_parties`            | Enjoyment of parties                           |
| `expressive`               | How expressive the person is                   |

### 🎯 Target Variable

**`personality_type`** – Categorical target with 3 classes:

- Introvert  
- Extrovert  
- Ambivert

---

## 🖼️ Visualizations

| Confusion Matrix | Class Distribution |
|------------------|--------------------|
| ![Confusion Matrix](report/confusion_matrix.png) | ![Class Balance](report/class_distribution.png) |

---

## 📡 Sample API I/O

### 🔐 Input (JSON)

```json
{
  "talking_often": 3,
  "comfortable_large_groups": 1,
  "likes_solitude": 5,
  "decision_thoughtful": 4,
  "likes_parties": 1,
  "expressive": 2
}


## 💭 Reflections
### ✅ Why did you choose this dataset?
This dataset is highly relatable and relevant in modern society. Personality insights can significantly impact team dynamics, education systems, recruitment processes, and mental health understanding. Its structure also makes it ideal for applying supervised classification models.

### 📚 What did you learn?
Techniques for cleaning and preprocessing behavioral survey data

Strategies for handling multi-class classification problems

Importance of addressing class imbalance and its effect on model fairness

Model evaluation using metrics like F1-score and confusion matrix

### 🚧 What were the challenges you encountered?
Class imbalance: The Ambivert class was notably underrepresented, requiring oversampling or class weighting

Overfitting: Tree-based models overfit quickly without pruning or regularization

Correlated features: Some input features were too similar and introduced redundancy

### 🔧 How would you improve your project?
Feature Expansion: Use NLP techniques on open-ended text or journal entries to enrich input data

Model Deployment: Wrap the trained model into an interactive web application using React + Flask

Data Collection: Launch a real-world anonymous survey to gather more diverse and modern responses

