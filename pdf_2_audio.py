import os
import PyPDF2
from gtts import gTTS

# Open the PDF file 
with open('document.pdf', 'rb') as file:
    # Create a PDF object
    reader = PyPDF2.PdfFileReader(file)

    # Iterate over every page in the PDF
    for page in range(reader.getNumPages()):
        text = reader.getPage(page).extractText()
        
        # Convert the text to audio format
        audio = gTTS(text)
        audio.save(f'Generated Speech.mp3')

