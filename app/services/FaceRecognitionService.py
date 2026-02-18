from retinaface import RetinaFace
from app.schemas.FaceRecognition import ImageInput
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

class FaceRecognitionService() :
    def image_processing(self, image) : 
        img = cv2.imread(image)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faces = RetinaFace.detect_faces(image)
        face_key = list(faces.keys())[1]
        bbox = faces[face_key]["facial_area"] 
        x1, y1, x2, y2 = bbox
        face_crop = img_rgb[y1:y2, x1:x2]
        return face_crop
    def  face_to_vector(self, face_crop):
        embedding = DeepFace.represent(self , face_crop, model_name="Facenet")
        return embedding
    def verify(embedded_face , selfie_crop) :
        result = DeepFace.verify(embedded_face, selfie_crop)
        return result['verified']
    def ceck_matching_faces(self , images : ImageInput ) :
        carteid_face = self.image_processing(images.carte_id)
        selfie_face = self.image_processing(images.selfie_image)
        embedded = self.face_to_vector(carteid_face)
        verifier = self.verify(embedded , selfie_face)
        return verifier



