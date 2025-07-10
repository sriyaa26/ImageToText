import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
import pyttsx3

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
for i, v in enumerate(voices):
    print(f"{i} - {v.name} | {v.id}")
voice_index = int(input("Enter the voice number you want to use: "))
engine.setProperty('voice', voices[voice_index].id)
engine.setProperty('rate', 150)            
engine.setProperty('volume', 1.0)         
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
pytesseract.pytesseract.tesseract_cmd = r"*tesseract location in your system*"
pdf = wi(filename="final_only.pdf", resolution=300)
pdfImage = pdf.convert('jpeg')
imageBlobs = []
for img in pdfImage.sequence:
    imgPage = wi(image=img)
    imageBlobs.append(imgPage.make_blob('jpeg'))
recognized_text = []
for imgBlob in imageBlobs:
    im = Image.open(io.BytesIO(imgBlob))
    text = pytesseract.image_to_string(im, lang='eng')
    recognized_text.append(text)
full_text = '\n'.join(recognized_text)
print(full_text)
speak(full_text)
with open('remember.txt', 'w') as f:
    f.write(full_text)
