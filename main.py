from googletrans import Translator
from PyPDF2 import PdfFileReader


def text_translator(text='Hello friend', src='en', dest='ru'):
    translator = Translator()
    translation = translator.translate(text=text, src=src, dest=dest)

    return translation.text


file_open = open('translate.pdf', 'rb')
pdf = PdfFileReader(file_open)
with open('translated.txt', 'w', encoding='UTF-8') as file:
    for i in range(0, pdf.getNumPages()):
        extractedText = pdf.getPage(i).extractText()
        content = extractedText.split('\n')
        for line in content:
            try:
                file.write(text_translator(text=line, src='en', dest='ru') + '\n')
            except Exception as ex:
                print('\n')

file_open.close()
file.close()