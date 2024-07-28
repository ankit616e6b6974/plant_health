from typing import List
from pydantic import BaseModel

from dto.nutrition_deficiency_res import NutritionDeficiency

class HealthStatus(BaseModel):
    HealthStatus : str | None = None
    NutritionDeficiencies: List[NutritionDeficiency] | None = None