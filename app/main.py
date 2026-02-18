from fastapi import FastAPI
from app.schemas.FaceRecognition import ImageInput
from app.controllers.FaceRecognitionController import FaceRecogntionController
app = FastAPI()

@app.post('/check_features')
def check_features(images : ImageInput) -> bool | str : 
    face_recognition = FaceRecogntionController().check_matched_features(images)
    return face_recognition