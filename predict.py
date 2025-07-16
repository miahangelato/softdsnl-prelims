import pandas as pd
import joblib

model = joblib.load("model.pkl")
le = joblib.load("label_encoder.pkl")

new_data = pd.read_csv("new_data.csv")

feature_cols = [
    'social_energy', 'alone_time_preference', 'talkativeness', 'deep_reflection',
    'group_comfort', 'party_liking', 'listening_skill', 'empathy', 'creativity',
    'organization', 'leadership', 'risk_taking', 'public_speaking_comfort',
    'curiosity', 'routine_preference', 'excitement_seeking', 'friendliness',
    'emotional_stability', 'planning', 'spontaneity', 'adventurousness',
    'reading_habit', 'sports_interest', 'online_social_usage', 'travel_desire',
    'gadget_usage', 'work_style_collaborative', 'decision_speed', 'stress_handling'
]

X_new = new_data[feature_cols]
y_pred_encoded = model.predict(X_new)
y_pred = le.inverse_transform(y_pred_encoded)

new_data['predicted_personality_type'] = y_pred
print(new_data[['predicted_personality_type']])

new_data.to_csv("predictions.csv", index=False)
