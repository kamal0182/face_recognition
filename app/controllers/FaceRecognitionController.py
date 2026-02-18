from app.services.FaceRecognitionService  import FaceRecognitionService
from schemas.FaceRecognition import ImageInput
class FaceRecogntionController() :
    def __init__(self):
        self.FaceRecognitionService = FaceRecognitionService()

    def check_matched_features(self, images : ImageInput) :
        matched = self.FaceRecognitionService.ceck_matching_faces(images)
        return matched
        

    