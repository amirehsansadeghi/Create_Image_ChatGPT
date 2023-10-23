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

input_text = input ( 'Please enter what are you think ? ')
size = input ('what size you whant ? (1024x1024 or 254x254) ')
number_of_the_image = input ('how many image you want create ? ')
number_of_the_image= int(number_of_the_image)
url1 = generate_photo_from_text(input_texttext,size,number_of_the_image)
response = requests.get(url1)
Image.open(response.raw)
