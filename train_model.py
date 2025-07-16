import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix, ConfusionMatrixDisplay, classification_report
)
import joblib

df = pd.read_csv("dataset.csv")

print(df['personality_type'].value_counts())
print(df[df['personality_type']=='Extrovert'].describe())
print(df[df['personality_type']=='Ambivert'].describe())

feature_cols = [
    'social_energy', 'alone_time_preference', 'talkativeness', 'deep_reflection',
    'group_comfort', 'party_liking', 'listening_skill', 'empathy', 'creativity',
    'organization', 'leadership', 'risk_taking', 'public_speaking_comfort',
    'curiosity', 'routine_preference', 'excitement_seeking', 'friendliness',
    'emotional_stability', 'planning', 'spontaneity', 'adventurousness',
    'reading_habit', 'sports_interest', 'online_social_usage', 'travel_desire',
    'gadget_usage', 'work_style_collaborative', 'decision_speed', 'stress_handling'
]

X = df[feature_cols]
le = LabelEncoder()
y = le.fit_transform(df["personality_type"])

print("Class distribution:")
print(df["personality_type"].value_counts())
print("Label encoder classes:", list(le.classes_))

plt.figure(figsize=(14,12))
corr = df[feature_cols].corr()
sns.heatmap(corr, cmap="coolwarm", annot=False, fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

sample_df = df.sample(n=min(500, len(df)), random_state=42)
sns.pairplot(sample_df, vars=['social_energy', 'talkativeness', 'empathy', 'leadership'],
             hue="personality_type", diag_kind="kde")
plt.suptitle("Pairplot of Selected Features by Personality Type", y=1.02)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
disp.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

decoded_preds = le.inverse_transform(y_pred)
print("\nSample Predictions:", decoded_preds[:10])

joblib.dump(model, "model.pkl")
joblib.dump(le, "label_encoder.pkl")
joblib.dump(feature_cols, "feature_columns.pkl")
print("✅ Model trained, evaluated, and saved.")
