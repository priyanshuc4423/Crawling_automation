import pyttsx3
import PyPDF2


with open("kaut.pdf","rb") as book:
    read_text = PyPDF2.PdfFileReader(book)
    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 100)

    for page in range(read_text.numPages):
        content = read_text.getPage(page)
        content_ext = content.extractText()

        audio_reader.say(content_ext)
        audio_reader.runAndWait()

