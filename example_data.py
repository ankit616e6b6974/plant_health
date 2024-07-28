# Mapping the data to the Pydantic models
from dto.health_status_res import HealthStatus
from dto.nutrition_deficiency_res import NutritionDeficiency

example_1 = HealthStatus(
    HealthStatus="Un-Healty",
    NutritionDeficiencies=[
        NutritionDeficiency(
            Name="Nitrogen deficiency",
            Description=" ",
            Solution=" "
        )
    ]
)

example_2 = HealthStatus(
    HealthStatus="Healty",
    NutritionDeficiencies=[
        NutritionDeficiency(
            Name="",
            Description="",
            Solution=""
        )
    ]
)