# 🎓 Final Prelim Activity: Build a Machine Learning API with Your Own Dataset

## 🧠 Objective

This activity is your final output for the Prelims. You will:

- Create or collect your own dataset (minimum 50 rows and 3 features)
- Visualize your dataset using **at least three types of visualizations**
- Train a machine learning model using **scikit-learn**
- Save the trained model and label encoder using **joblib**
- Build a Django REST API that serves predictions based on your model
- Test the API using **Postman**
- Submit a well-documented GitHub repository

---

## ✅ Requirements

### 📊 Dataset

- Minimum of **50 rows**
- At least **3 numeric features**
- One target column (label/class to predict)
- Can be:
  - Created manually (CSV)
  - Collected from a public source (e.g., UCI, Kaggle)
  - Synthesized or simulated (e.g., random numeric traits and labels)
- Save the file as `dataset.csv`

---

### 📈 Visualizations

You must include **at least 3 different visualizations**, such as:
- Histogram
- Pairplot
- Correlation heatmap
- Boxplot
- Scatterplot
- Confusion matrix (for classification)

Use any combination of `matplotlib`, `seaborn`, or `pandas`.

---

### 🧪 Model Training

Create a script named `train_model.py` that:
- Loads the dataset from `dataset.csv`
- Encodes the label if needed (using `LabelEncoder`)
- Trains a model (e.g., RandomForestClassifier or other)
- Saves the trained model as `model.pkl`
- Saves the label encoder as `label_encoder.pkl` (if applicable)
- Generates and saves visualizations (optional)

---

### 🌐 Django API

Build a Django REST API with the following:

- A single endpoint: `POST /api/predict/`
- Accepts 3 feature inputs via JSON
- Loads `model.pkl` and `label_encoder.pkl`
- Returns a prediction (decoded label or numeric value)

Use Django REST Framework for the API logic.

You do **not** need to deploy the API. Just run locally and test with Postman.

---

## 📁 Recommended Folder Structure

```
final-ml-api-project/
├── dataset.csv                   # Your dataset
├── train_model.py                # Loads data, visualizes, trains and saves model
├── model.pkl                     # Saved model
├── label_encoder.pkl             # Saved label encoder (if used)
├── requirements.txt              # All libraries used
├── README.md                     # This file
├── report/                       # Screenshots folder
│   ├── visualization1.png
│   ├── visualization2.png
│   ├── visualization3.png
│   ├── postman1.png
│   ├── postman2.png
│   └── ...
└── ml_api_project/               # Django REST API project
    ├── manage.py
    ├── ml_api_project/
    │   ├── settings.py
    │   └── urls.py
    └── ml_api/
        ├── views.py
        ├── urls.py
        ├── apps.py
        └── ...
```

---

## 🧪 Sample Postman Test

POST to: `http://localhost:8000/api/predict/`

**JSON body example:**
```json
{
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4
}
```

**Sample response:**
```json
{
  "prediction": "setosa"
}
```

Take at least **2–3 screenshots** of valid request/response results and include them in the `report/` folder or embed them in the README.

---

## 📝 What to Submit

- A GitHub repository with:
  - `dataset.csv`
  - `train_model.py`
  - Saved `.pkl` files
  - Working Django project with API
  - `requirements.txt`
  - At least 3 visualizations
  - A `report/` folder or embedded screenshots in the README
  - This completed `README.md`

---

## 📄 README Format (this file)

Make sure your `README.md` includes the following:

- **Project Title and Description**
- **Description of your dataset**
- **Description of features and target label**
- **Screenshots of visualizations (or linked images from `report/`)**
- **Sample API input/output (Postman screenshots or JSON)**
- **Reflection answers:**
  - Why did you choose this dataset?
  - What did you learn?
  - What were the challenges you encountered?
  - How would you improve your project?

---

## 📦 How to Run

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python train_model.py
```

### 4. Run the Django server

```bash
cd ml_api_project
python manage.py runserver
```

---

## 🧠 Grading Rubric (100 pts)

| Criteria                                  | Points |
|-------------------------------------------|--------|
| Dataset meets requirements                | 15     |
| At least 3 unique visualizations included | 20     |
| Model trains and saves correctly          | 15     |
| API works and returns correct prediction  | 25     |
| At least 2 working Postman tests          | 10     |
| Organized project structure               | 5      |
| README documentation                      | 5      |
| Reflection answers                        | 5      |
| **TOTAL**                                 | **100** |

---

## 🙌 Good luck, and build something you're proud of!
