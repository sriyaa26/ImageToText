# 🗣️ PDF & Image Text Reader with Text-to-Speech

A Python-based assistant that extracts text from scanned PDFs or images using **Tesseract OCR**, then reads it aloud using **Text-to-Speech**. Built for accessibility, education, and productivity.



 🔍 Features

- ✅ Extracts text from scanned **PDF files**
- 🖼️ Reads **image-based documents** (`.jpg`, `.png`, etc.)
- 🗣️ Speaks the extracted text aloud using **offline TTS**
- 🎛️ Supports *voice selection*, *speech rate*, and *volume control*
- 💾 Saves recognized text to a `.txt` file
- 📦 Works completely **offline** after setup



 🧰 Technologies Used

 `Python`
`pytesseract` – Python binding for Tesseract OCR
 `pyttsx3` – Text-to-Speech engine (Windows SAPI5)
`Pillow` – Image handling
 `wand` – PDF to image conversion using ImageMagick
 `Tesseract-OCR` – For recognizing text
 `ImageMagick` – For converting PDFs to images


