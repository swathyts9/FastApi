import httpx
from config import REPLICATE_API_KEY, REPLICATE_BASE_URL, MODEL_VERSION_NAME

async def generate_image(prompt: str, version: str):
    headers = {
        "Authorization": f"Token {REPLICATE_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "version": f"{MODEL_VERSION_NAME}", # Use the actual model version ID here
        "input": {
            "prompt": prompt
        }
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(REPLICATE_BASE_URL, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result["output"]  # This assumes the output contains the image URL
        except httpx.HTTPStatusError as e:
            print("Error response from Replicate API:", e.response.json())  # Debugging line
            raise