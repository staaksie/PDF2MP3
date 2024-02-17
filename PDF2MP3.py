import PyPDF2, pyttsx3

reader = PyPDF2.PdfReader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()

cleanText = ''
for page in range(len(reader.pages)):
    text = reader.pages[page].extract_text()
    cleanText += text.strip().replace('\n', ' ')
    print(cleanText)


speaker.save_to_file(cleanText, 'story.mp3')
speaker.runAndWait()

speaker.stop()    
