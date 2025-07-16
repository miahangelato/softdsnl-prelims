from ninja import Schema

class PredictRequest(Schema):
    social_energy: float
    alone_time_preference: float
    talkativeness: float
    deep_reflection: float
    group_comfort: float
    party_liking: float
    listening_skill: float
    empathy: float
    creativity: float
    organization: float
    leadership: float
    risk_taking: float
    public_speaking_comfort: float
    curiosity: float
    routine_preference: float
    excitement_seeking: float
    friendliness: float
    emotional_stability: float
    planning: float
    spontaneity: float
    adventurousness: float
    reading_habit: float
    sports_interest: float
    online_social_usage: float
    travel_desire: float
    gadget_usage: float
    work_style_collaborative: float
    decision_speed: float
    stress_handling: float

class PredictResponse(Schema):
    prediction: str