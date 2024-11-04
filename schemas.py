# schemas.py
from pydantic import BaseModel

class ImageGenerationRequest(BaseModel):
    prompt: str
    model: str = "stability-ai/stable-diffusion"  # default model

class ImageGenerationResponse(BaseModel):
    image_url: str