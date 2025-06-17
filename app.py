import os
import gradio as gr
import requests
import io
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from the .env file
load_dotenv()

API_URL = os.environ.get("API_URL")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

# Set the authorization header
headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}

def query(payload):

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
    )

    return response.content


# Function to generate an image from a given prompt
def generate_image(prompt):
    image_bytes = query({"inputs": prompt})  # Get image bytes from the API response
    
    
    image = Image.open(io.BytesIO(image_bytes))  # Open the image from the byte data

    return image


# Create a Gradio interface
demo = gr.Interface(
    fn=generate_image,
    inputs="text",
    outputs="image",
)

# demo.launch(share=True)
demo.launch(server_name="0.0.0.0", server_port=7860)

