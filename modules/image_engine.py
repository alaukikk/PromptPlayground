import requests
from io import BytesIO
from urllib.parse import quote
from PIL import Image

def generate_image(prompt):
    # Public third-party endpoint; availability and rate limits are not guaranteed.
    url = "https://image.pollinations.ai/prompt/" + quote(prompt, safe="")
    response = requests.get(url, params={"width": 768, "height": 768, "nologo": "true"}, timeout=120)
    response.raise_for_status()
    if "image" not in response.headers.get("content-type", ""):
        raise RuntimeError("Image service returned a non-image response.")
    return Image.open(BytesIO(response.content)).convert("RGB")
