import os
import requests
import json
import argparse
from langdetect import detect


MS_TRANSLATOR_KEY = os.environ.get("MS_TRANSLATOR_KEY")


def main(text, dest_language):
    source_lang = source_language(text)
    translated_text = translate_text(text, source_lang, dest_language)
    print(f"Translation: {translated_text}")


def command_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--language", dest="dest_language", required=True, help="Destination language code")
    parser.add_argument("text", help="Text to translate")
    args = parser.parse_args()
    return args


def source_language(text):
    return detect(text)


def translate_text(text, source_language, dest_language):
    if not os.environ.get("MS_TRANSLATOR_KEY"):
        raise RuntimeError("Translation service is not configured")
    auth = {
        'Ocp-Apim-Subscription-Key': os.environ.get("MS_TRANSLATOR_KEY"),
        'Ocp-Apim-Subscription-Region': 'southafricanorth'}
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com'
        '/translate?api-version=3.0&from={}&to={}'.format(
            source_language, dest_language), headers=auth, json=[
                {'Text': text}])
    if r.status_code != 200:
        return 'Error: the translation service failed.'
    return r.json()[0]['translations'][0]['text']



if __name__=="__main__":
    args = command_parser()
    main(args.text, args.dest_language)
