import openai as OpenAI
from dotenv import load_dotenv
from PIL import Image
import os 

#load all defination data from .env file to memory 
load_dotenv()

#load secret key from .env file secret key field 
secret_key=os.getenv('secret_key')

OpenAI.api_key=secret_key

def generate_photo_from_text(text,Size,number):
    response = OpenAI.Image.create(
    prompt=text,
     n=number,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']

    return image_url

text = "batman art in red and blue color"
url1 = generate_photo_from_text(text,"1024x1024",1)
response = requests.get(url1)
Image.open(response.raw)
