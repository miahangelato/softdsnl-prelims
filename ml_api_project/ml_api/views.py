from ninja import NinjaAPI
import joblib
import os
from django.conf import settings
from .schema import PredictRequest, PredictResponse

model_path = os.path.join(settings.BASE_DIR, "ml_api", "model.pkl")
encoder_path = os.path.join(settings.BASE_DIR, "ml_api", "label_encoder.pkl")

model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

api = NinjaAPI()

@api.post("/predict", response=PredictResponse)
def predict(request, data: PredictRequest):
    input_features = [
        data.social_energy, data.alone_time_preference, data.talkativeness,
        data.deep_reflection, data.group_comfort, data.party_liking,
        data.listening_skill, data.empathy, data.creativity, data.organization,
        data.leadership, data.risk_taking, data.public_speaking_comfort,
        data.curiosity, data.routine_preference, data.excitement_seeking,
        data.friendliness, data.emotional_stability, data.planning,
        data.spontaneity, data.adventurousness, data.reading_habit,
        data.sports_interest, data.online_social_usage, data.travel_desire,
        data.gadget_usage, data.work_style_collaborative, data.decision_speed,
        data.stress_handling
    ]
    prediction_encoded = model.predict([input_features])
    prediction_label = label_encoder.inverse_transform(prediction_encoded)[0]
    return {"prediction": prediction_label}
