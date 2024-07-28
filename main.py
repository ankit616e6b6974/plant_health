#from typing import List
from fastapi import FastAPI, File, UploadFile, HTTPException
#from pydantic import BaseModel
#from fastapi.responses import JSONResponse
#from PIL import Image
#import io
#import pickle
#import numpy as np
#import torch
#from torchvision import transforms

from dto.health_status_res import HealthStatus
from dto.nutrition_deficiency_res import NutritionDeficiency
import example_data
from utils.config import get_config
#from utils.model import ResNet9
#from utils.disease import disease_dic
from dotenv import load_dotenv

# Load environment variables from the .env file
config = get_config()

# Initialize FastAPI app
app = FastAPI()

# Endpoint for predicting nutrient deficiencies
@app.post("/predict-deficiency", response_model=HealthStatus)
async def predict(file: UploadFile = File(...)):
    try:
        # Read the uploaded file and convert it to an image
        health_status = HealthStatus()

        if config.ENVIROMENT == "dummey":
            health_status = example_data.example_1
        
        # TODO: Logic to get health        
        return health_status

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the server with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=config.APP_PORT)
