from pydantic import BaseModel  , field_validator
from fastapi import UploadFile
from PIL import Image
import io



class ImageInput(BaseModel):
    carte_id: UploadFile
    selfie_image : UploadFile

    @field_validator("carte_id","selfie_image")
    @classmethod
    def validate_image(cls, file: UploadFile , selfie_image):
        if file.content_type not in ["image/jpeg", "image/png"]:
            raise ValueError("File must be JPEG or PNG")
        contents = file.file.read()
        try:
            Image.open(io.BytesIO(contents))
        except Exception:
            raise ValueError("Invalid image file")
        file.file.seek(0)  
        return file
