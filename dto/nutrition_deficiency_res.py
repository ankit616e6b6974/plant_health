from pydantic import BaseModel

class NutritionDeficiency(BaseModel):
    Name: str | None = None
    Description: str | None = None
    Solution: str | None = None