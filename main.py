from fastapi import FastAPI, HTTPException
from schemas import ImageGenerationRequest, ImageGenerationResponse
from services import generate_image
import httpx

app = FastAPI(title="Image Generation API with Replicate", version="1.0")

@app.post("/generate-image", response_model=ImageGenerationResponse)
async def generate_image_endpoint(request: ImageGenerationRequest):
    """
    Generate an image based on the provided prompt using Replicate's model.
    """
    
    try:
        image_url = await generate_image(request.prompt, request.model)
        return ImageGenerationResponse(image_url=image_url)
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Failed to generate image")