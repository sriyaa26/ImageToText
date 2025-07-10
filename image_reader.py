import pytesseract
from PIL import Image
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r"*location of tesseract in your system*"


img = Image.open('"your image name".jpg')  
text = pytesseract.image_to_string(img)
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
for i, v in enumerate(voices):
    print(f"{i} - {v.name} | {v.id}")
voice_index = int(input("Enter the voice number you want to use: "))
engine.setProperty('voice', voices[voice_index].id)
print("Extracted Text:\n", text)
engine.setProperty('rate', 150)           
engine.setProperty('volume', 1.0)         
engine.say(text)
engine.runAndWait()
with open('image_text.txt', 'w') as f:
    f.write(text)
