from pydantic import BaseModel


class PredictionResponse(BaseModel):
    sentiment: str
