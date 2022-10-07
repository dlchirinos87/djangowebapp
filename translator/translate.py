from googletrans import Translator


def translate_text(input_text):
    translator = Translator()
    translated_text = translator.translate(text=input_text, dest='es')
    return translated_text.text

